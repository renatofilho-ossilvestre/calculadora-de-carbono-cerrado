# calculadora-de-carbono-cerrado
Projeto: Migração de Modelo de Emissões de Carbono (Excel → Python)
🌱 AgroCarbon – Estimativa de Carbono em Árvores
Projeto em Python para estimar biomassa, carbono e CO₂ a partir de dados de árvores (diâmetro, altura e densidade da madeira).

📌 Objetivo
Transformar medições simples de campo em estimativas de:

Biomassa (kg)

Carbono (kg)

CO₂ equivalente (kg)

Utilizando equações alométricas amplamente usadas na literatura científica.

⚙️ Como funciona
Entrada:

Arquivo CSV ou Excel com dados das árvores

Processamento:

Aplicação de fórmula alométrica

Saída:

Novo CSV com colunas calculadas

📐 Fórmula utilizada
Biomassa:

biomassa = 0.0673 * (densidade * D² * H)^0.976
Onde:

D = diâmetro (cm)

H = altura (m)

densidade = densidade da madeira (g/cm³)

Conversões:

carbono = biomassa × 0.47

CO₂ = carbono × 3.67

📂 Estrutura do projeto
projeto/
├─ src/
│  └─ agrocarbon/
│     ├─ model.py
│     ├─ cli.py
│     └─ __init__.py
├─ teste/
│  ├─ renato.csv
│  └─ testett.py
├─ tests/
│  └─ test_model.py
▶️ Como executar
1. Instalar dependências
pip install pandas typer rich openpyxl
2. Rodar script simples
Dentro da pasta teste:

python testett.py
3. Rodar via CLI
Na raiz do projeto:

$env:PYTHONPATH="src"
python -m agrocarbon.cli -i entrada.csv -o saida.csv
📥 Formato de entrada
CSV ou Excel com colunas:

dap_cm,altura_m,densidade
Exemplo:

30,15,0.6
20,10,0.5
📤 Saída
Arquivo com novas colunas:

biomassa_kg
carbono_kg
co2_kg
⚠️ Observações
A densidade da madeira pode variar por espécie

Caso não tenha, pode usar valor médio (~0.6)

Para maior precisão, integrar tabela de densidade por espécie

🚀 Próximos passos
Integrar base de densidade por espécie

Melhorar modelo por bioma (Amazônia, Cerrado, etc.)

Calcular sequestro anual de carbono

Criar interface web ou API

📚 Referência
Chave et al. (2014) – Allometric models for estimating tree biomass

👨‍💻 Autor
Projeto em desenvolvimento para aplicaçõ
