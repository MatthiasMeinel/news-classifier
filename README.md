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

## 📁 Estrutura do Projeto

Project/
│
├── api/ # API FastAPI
├── src/ # Funções e lógica do modelo
├── notebook/ # EDA e treinamento
├── data/ # (não incluído no repo)
├── models/ # (não incluído no repo)






