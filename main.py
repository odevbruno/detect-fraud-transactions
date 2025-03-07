import time
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

path = './assets/data.csv'

# Gera os dados para treinar e testar a LM
def generate_data(rpt=100):
  data = pd.DataFrame({
    "valor": np.random.randint(100, 100000, rpt),
    "horario": np.random.randint(0, 23, rpt),
  })
  
  data['fraude'] = (
    (data['valor'] > 30000) & 
    (data['horario'] < 7)
  ).astype(int)
  
  data.to_csv(path, index=False)
  return data
   
# Treina o modelo 
def traine_model(data):
  X = data.drop('fraude', axis=1)
  y = data['fraude']
  
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  
  model = RandomForestClassifier()
  model.fit(X_train, y_train)
  
  y_pred = model.predict(X_test)      
  
  print(f"Acurácia: {accuracy_score(y_test, y_pred) * 100:.2f}%")
  joblib.dump(model, './assets/model.pkl')

# Detecta fraudes usando o modelo criado
def detect(transaction):
  feature_names = ['valor', 'horario']
  transaction_df = pd.DataFrame([transaction], columns=feature_names)
  model = joblib.load('./assets/model.pkl')
  res = model.predict(transaction_df)
  return res

def handle_generate():
  print("📦 - Gerando dados para simular transações reais")
  time.sleep(2)
  
  data_test = generate_data(100)
  print(f"✅ - Dados gerados: {data_test['fraude'].value_counts()}")
  time.sleep(2)
  
  
def handle_traine_model():
  data = pd.DataFrame(pd.read_csv(path))
  traine_model(data)
  
def handle_detect():
  print("⏲️ - Iniciando a detecção de transações fraudulentas...")
  time.sleep(2)
  
  data = pd.read_csv(path).drop('fraude', axis=1)
  data_list = data.to_numpy()

  fraudes_detected = []

  for index, value in enumerate(data_list):
    [isFraud] = detect(value)
    if isFraud:
      fraudes_detected.append(index)
      
  print("Transações fraudulentas:")   
  for i in fraudes_detected:
    print(f"❌ - Transação {i}: {data_list[i]}")  
  
  time.sleep(2)
  print(f"Foram detectadas {len(fraudes_detected)} fraudes")    
  
# Gera dados para treinar a LM e tbm para realizar o teste no modelo
handle_generate()

# Ativar quando quiser treinar o modelo 
# handle_traine_model()

# Detectando as fraudes usando o modelo ja treinado
handle_detect()  
  
