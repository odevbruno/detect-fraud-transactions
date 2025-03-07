# 🚀 Detector de fraudes em transações financeiras com Python e Machine Learning

## 📌 Sobre o Projeto
Este projeto é um **detector de fraudes simples** desenvolvido como parte dos meus estudos em **Python e Machine Learning**. O objetivo é identificar transações suspeitas com base em um modelo de aprendizado de máquina.

## 🛠 Tecnologias Utilizadas
- **Python** 🐍
- **pandas** 📊 (Manipulação de dados e CSV)
- **NumPy** 🔢 (Criação de dados aleatórios)
- **scikit-learn** 🤖 (Treinamento do modelo com Random Forest)
- **joblib** 💾 (Salvar e carregar o modelo treinado)

## 📂 Estrutura do Projeto
```
📁 projeto/
│-- 📁 assets/          # Contém os arquivos CSV e o modelo treinado
│-- 📄 main.py         # Código principal do projeto
│-- 📄 README.md       # Documentação do projeto
```

## 🔧 Como Usar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/fraud-detector.git
cd fraud-detector
```

### 2️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Gerar dados para treino e teste
```python
from main import handle_generate
handle_generate()
```
Isso criará um arquivo `data.csv` na pasta `assets/` contendo transações simuladas.

### 4️⃣ Treinar o modelo
```python
from main import handle_traine_model
handle_traine_model()
```
Isso criará um modelo treinado e salvará como `model.pkl`.

### 5️⃣ Testar a detecção de fraudes
```python
from main import handle_detect
handle_detect()
```
Isso analisará as transações e imprimirá as que foram identificadas como fraudulentas.

## 📊 Lógica de Detecção
O modelo foi treinado para marcar como **fraude** transações que atendam a este critério:
- Valor acima de **30.000** 💰
- Horário da transação entre **00h e 06h** ⏰

## 📌 Próximos Passos
✅ Melhorar o modelo com mais features e ajuste de hiperparâmetros.
✅ Implementar visualizações gráficas dos resultados.
✅ Integrar com um banco de dados real para testes.

💡 Sugestões e contribuições são bem-vindas! 😃

---

📢 **Gostou do projeto?** Deixe uma ⭐ no repositório e contribua! 🚀

