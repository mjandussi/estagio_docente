import re
from io import BytesIO
import pandas as pd

def limpar_nome_aba(nome: str) -> str:
    # remove caracteres inválidos para nome de aba do Excel
    nome = re.sub(r'[:\\/*?\[\]]', '_', nome)
    # limita a 31 caracteres
    nome = nome[:31]
    return nome

def exportar_razoes_para_excel(razoes_dict: dict) -> BytesIO:
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        resumo = []

        for conta, df in razoes_dict.items():
            df_export = df.copy()

            for col in ["Histórico", "Débito", "Crédito"]:
                if col not in df_export.columns:
                    df_export[col] = ""

            nome_aba = limpar_nome_aba(conta)
            df_export.to_excel(writer, sheet_name=nome_aba, index=False)

            deb = pd.to_numeric(df_export["Débito"], errors="coerce").fillna(0).sum()
            cred = pd.to_numeric(df_export["Crédito"], errors="coerce").fillna(0).sum()
            saldo = deb - cred

            resumo.append({
                "Conta": conta,
                "Nome da Aba": nome_aba,
                "Total Débito": deb,
                "Total Crédito": cred,
                "Saldo": abs(saldo),
                "Natureza do Saldo": "Devedor" if saldo >= 0 else "Credor"
            })

        df_resumo = pd.DataFrame(resumo)
        df_resumo.to_excel(writer, sheet_name="Resumo", index=False)

    output.seek(0)
    return output


def importar_razoes_de_excel(arquivo_upload, contas_fixas: list) -> dict:
    xls = pd.ExcelFile(arquivo_upload)
    razoes_importadas = {}

    mapa_abas = {limpar_nome_aba(conta): conta for conta in contas_fixas}

    for aba in xls.sheet_names:
        if aba == "Resumo":
            continue

        if aba in mapa_abas:
            conta_real = mapa_abas[aba]
            df = pd.read_excel(xls, sheet_name=aba)

            if "Histórico" not in df.columns:
                df["Histórico"] = ""
            if "Débito" not in df.columns:
                df["Débito"] = 0.0
            if "Crédito" not in df.columns:
                df["Crédito"] = 0.0

            df = df[["Histórico", "Débito", "Crédito"]]
            razoes_importadas[conta_real] = df

    return razoes_importadas