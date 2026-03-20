from pathlib import Path
import pandas as pd

# caminho do arquivo CSV
path = Path(__file__).parent / "dados.csv"

# ler CSV
df = pd.read_csv(path, sep=";", encoding="latin1", on_bad_lines="skip")

# -------------------------
# SIMULAÇÃO DE DADOS DE CAMPO
# (substitua depois pelos seus dados reais)
# -------------------------
df["dap_cm"] = 30        # diâmetro (cm)
df["altura_m"] = 15      # altura (m)
df["densidade"] = 0.6    # densidade média

# -------------------------
# CÁLCULO DE CARBONO
# -------------------------
df["biomassa_kg"] = 0.0673 * (df["densidade"] * (df["dap_cm"]**2) * df["altura_m"])**0.976
df["carbono_kg"] = df["biomassa_kg"] * 0.47
df["co2_kg"] = df["carbono_kg"] * 3.67

# -------------------------
# RESULTADO
# -------------------------
print(df[["nome_cientifico", "biomassa_kg", "carbono_kg", "co2_kg"]].head())

# salvar resultado
output_path = Path(__file__).parent / "resultado.csv"
df.to_csv(output_path, index=False)

print("\nArquivo salvo em:", output_path)