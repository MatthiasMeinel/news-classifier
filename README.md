# 📰 Classificador de Notícias

## 📌 Descrição

Este projeto tem como objetivo desenvolver um sistema de classificação automática de categorias de notícias utilizando técnicas de Processamento de Linguagem Natural (NLP).

A solução contempla todo o ciclo de um projeto de dados, desde a análise exploratória até a disponibilização do modelo via API.

---

## 🚀 Funcionalidades

- Análise exploratória dos dados (EDA)
- Pré-processamento de texto
- Treinamento de modelo de classificação
- Avaliação com métricas (precision, recall, f1-score)
- API REST para predição em tempo real

---

## 🧠 Metodologia

O projeto foi desenvolvido em três etapas principais:

### 1. Análise Exploratória (EDA)
- Verificação de valores nulos
- Distribuição das categorias
- Análise do tamanho dos textos
- Identificação de desbalanceamento entre classes

### 2. Modelagem
- Vetorização de texto com **TF-IDF**
- Modelo de classificação com **Regressão Logística**
- Divisão treino/teste
- Avaliação com métricas de classificação

### 3. Deploy
- Criação de API utilizando **FastAPI**
- Endpoint para predição de novas notícias

---

## 📊 Resultados

O modelo apresentou:

- **Accuracy:** ~84%
- Bom desempenho em categorias com maior volume de dados
- Desempenho reduzido em classes com poucos exemplos (devido ao desbalanceamento)

---

## ⚙️ Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib

---

## 📦 Dataset

O dataset não está incluído neste repositório devido às limitações de tamanho do GitHub.

Para reproduzir os resultados, é necessário disponibilizar o arquivo de dados na pasta `data/`.

O arquivo usado para o treinamento do modelo foi esse: https://www.kaggle.com/datasets/marlesson/news-of-the-site-folhauol

---

## 🤖 Modelo

O modelo treinado não foi versionado devido ao seu tamanho. 

Ele pode ser facilmente reproduzido executando o notebook de treinamento presente em `notebook'





## 📁 Estrutura do Projeto

Project/
│
├── api/ # API FastAPI
├── src/ # Funções e lógica do modelo
├── notebook/ # EDA e treinamento
├── data/ # (não incluído no repo)
├── models/ # (não incluído no repo)






