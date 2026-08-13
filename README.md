# 👴 Sistema de Detecção e Classificação de Quedas em Idosos

> **Visão Computacional em Tempo Real** | Detecção automática de eventos de queda com minimização de falsos positivos em Atividades de Vida Diária (AVDs)

[![Interativo](https://img.shields.io/badge/Interface-Interativa-blue?style=flat-square)](https://pahsantana.github.io/LAB-CV2026.2/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Latest-red?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green?style=flat-square&logo=opencv)](https://opencv.org/)

---

## 📑 Índice Rápido

- [Visão Geral](#-visão-geral)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Conteúdo dos Laboratórios](#-conteúdo-dos-laboratórios)
- [Projeto Final](#-projeto-final)
- [Resultados](#-métricas-e-resultados-experimentais)
- [Como Usar](#-instruções-de-execução)
- [Declaração IA](#-declaração-de-integridade)

---

## 🎯 Visão Geral

Este repositório contém a **documentação técnica completa**, **8 módulos de aprendizado prático** (Laboratórios), **scripts do projeto final** e **validação com voluntários** de um sistema inteligente de detecção de quedas em tempo real.

### Destaques
✅ Detecção em **tempo real** (RGB)  
✅ Execução em **CPU** (Edge Processing)  
✅ Minimização de **falsos positivos** em AVDs  
✅ Validação com **voluntários reais**  
✅ Interface **interativa** web  

**🔗 [Acesse a página interativa do projeto](https://pahsantana.github.io/LAB-CV2026.2/)**

---

## 📁 Estrutura do Repositório

```
LAB-CV2026.2/
│
├── 📚 Laboratórios (Labs)
│   ├── lab1_arquivos/           ↳ Fundamentos de Imagem e Histogramas
│   ├── lab2_arquivos/           ↳ Filtragem Espacial e Convolução
│   ├── lab3_arquivos/           ↳ Detecção de Bordas e Transformada Hough
│   ├── lab4_arquivos/           ↳ Morfologia Matemática e Segmentação
│   ├── lab5_arquivos/           ↳ Características (SIFT/ORB) e Contornos
│   ├── lab6_arquivos/           ↳ Transformações Geométricas e Calibração
│   ├── lab7/                    ↳ Fluxo Óptico e Rastreamento
│   └── lab8_arquivos/           ↳ CNNs e Detecção de Objetos
│
├── 📊 Projeto Final
│   ├── projeto/
│   │   ├── pics/                ↳ Dataset fotográfico
│   │   └── refs/                ↳ Documentação e referências
│   │
│   ├── teste_voluntarios/       ↳ Validação prática
│   │   ├── logs/                ↳ Registros cinemáticos (.csv)
│   │   ├── videos/              ↳ Ensaios em tempo real (.mp4)
│   │   └── teste-voluntarios-dados.ipynb
│   │
│   ├── trabalho_final.ipynb     ↳ Pipeline completo
│   └── artigo-grupo1-quedaidosos.pdf
│
├── 📄 Documentação
│   ├── index.html               ↳ Interface web
│   ├── roteiro_teste_detector_quedas.pdf
│   └── README.md                ↳ Este arquivo
│
└── ⚙️ Configuração
    └── requirements.txt         ↳ Dependências Python
```

---

## 🧪 Conteúdo dos Laboratórios

| Lab | Tema | Tópicos Principais |
|-----|------|-------------------|
| **Lab 1** | 🖼️ Fundamentos de Imagem | Espaços de cor (RGB, HSV, Grayscale), manipulação de pixels, histogramas |
| **Lab 2** | 🔧 Filtragem Espacial | Convoluções 2D, Blur, Gaussian, Median, Sharpening |
| **Lab 3** | 📐 Detecção de Bordas | Sobel, Laplaciano, Canny, Transformada de Hough |
| **Lab 4** | 🎭 Morfologia Matemática | Erosão, Dilatação, Abertura, Fechamento, Limiarização |
| **Lab 5** | 🔑 Extração de Características | SIFT/ORB, Keypoints, Contornos, Pareamento |
| **Lab 6** | 📐 Transformações Geométricas | Homografia, Perspectiva, Calibração de câmeras |
| **Lab 7** | 🎬 Fluxo Óptico e Rastreamento | Lucas-Kanade, Farneback, Tracking de objetos |
| **Lab 8** | 🧠 Redes Neurais Convolucionais | Arquiteturas CNN, Detecção em tempo real |

---

## ⚙️ Projeto Final: Arquitetura da Solução

### 🎯 Objetivo
Detectar automaticamente quedas de idosos em **tempo real**, minimizando falsos positivos em Atividades de Vida Diária (AVDs) como agachar ou sentar.

### 🏗️ Pipeline Técnico

```
┌─────────────────────────────────────────────────────────────────┐
│ 1️⃣  RASTREAMENTO DE PESSOAS                                      │
│     └─ SSDLite320 MobileNetV3 (CPU-optimized, Edge Processing) │
├─────────────────────────────────────────────────────────────────┤
│ 2️⃣  ANÁLISE CINEMÁTICA                                           │
│     └─ Extração de: Centroide, Velocidade (v), Deslocamento (Δy),
│                     Razão de Aspecto (w/h)                        │
├─────────────────────────────────────────────────────────────────┤
│ 3️⃣  MOTOR DE DECISÃO MULTICRITÉRIO                              │
│     └─ Janela Temporal: 1,55s                                    │
│     └─ Critério: ≥ 3 de 4 parâmetros acima do limiar crítico    │
├─────────────────────────────────────────────────────────────────┤
│ 4️⃣  CLASSIFICAÇÃO FINAL                                          │
│     └─ QUEDA | NÃO QUEDA | NÃO CLASSIFICADO                     │
└─────────────────────────────────────────────────────────────────┘
```

### 📊 Métricas e Resultados Experimentais

#### Comparação de Performance

| Métrica | Log Legado | Bancada | Log Atual |
|---------|-----------|--------|-----------|
| **Padrão de Transição** | `em_pé → deitado` | `em_pé → agachado` | `múltiplas` |
| **Janela Temporal (t)** | ≈ 0,18–0,20 s | ≈ 1,50–1,59 s | **1,55 s** (padronizado) |
| **Velocidade (v)** | 0,0 a -6,7 px/s | 0,8 a 5000,0 px/s | até 5500,0 px/s |
| **Confiança** | — | 0,71–1,00 | **0,88–0,99** ✅ |
| **Classificação** | DEITOU_VOLUNTARIAMENTE | Flutuação | EVENTO_NÃO_CLASSIFICADO ✅ |

#### 🎯 Conclusão de Usabilidade
Em movimentos de agachamento rápido, picos isolados de velocidade (**5500,0 px/s**) foram **descartados com sucesso** (pontuação 2/4), evitando **falsos alarmes** em AVDs.

---

## 🚀 Instruções de Execução

### ✅ Pré-requisitos

```bash
Python 3.9+
Jupyter Notebook / JupyterLab
```

### 📦 Instalação de Dependências

```bash
pip install -r requirements.txt
```

**Ou instale manualmente:**

```bash
pip install opencv-python torch torchvision pandas numpy matplotlib jupyter
```

### ▶️ Executar o Pipeline Completo

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/LAB-CV2026.2.git
cd LAB-CV2026.2

# Iniciar Jupyter Notebook
jupyter notebook trabalho_final.ipynb
```

O notebook irá:
1. Carregar o modelo SSDLite320 MobileNetV3
2. Processar fluxo de vídeo RGB
3. Extrair cinemática de cada frame
4. Aplicar filtro multicritério
5. Gerar relatório de eventos

### 📊 Analisar Dados dos Voluntários

```bash
jupyter notebook teste_voluntarios/teste-voluntarios-dados.ipynb
```

Visualizará:
- 📈 Consolidação gráfica dos logs
- 📉 Métricas da Escala SUS
- 📌 Análise estatística dos ensaios

---

## 📚 Arquivos Principais

| Arquivo | Descrição |
|---------|-----------|
| `trabalho_final.ipynb` | 🔥 **Pipeline completo** — Execute aqui! |
| `teste_voluntarios/teste-voluntarios-dados.ipynb` | 📊 Análise e validação prática |
| `artigo-grupo1-quedaidosos.pdf` | 📄 Relatório científico formal |
| `index.html` | 🌐 Interface interativa web |
| `roteiro_teste_detector_quedas.pdf` | 📋 Metodologia dos testes |

---

## 📜 Declaração de Integridade e Uso de IA Generativa

Em cumprimento rigoroso à **Portaria CNPq nº 2.664/2026** (Artigo 2º, alíneas c, d e f):

### 🤖 Ferramentas de IA Generativa Utilizadas

| Ferramenta | Fase | Finalidade |
|-----------|------|-----------|
| **Claude** (Anthropic) | Desenvolvimento de Código | Estruturação, refatoração, sintaxe e otimização dos algoritmos Python/Jupyter |
| **Gemini** (Google) | Redação e Análise de Dados | Síntese de logs, análise estatística, revisão técnica e padronização |

### ✍️ Autoria e Controle Humano

✅ **Escopo Conceitual**: Integralmente concebido pelos autores  
✅ **Modelagem de Algoritmos**: Implementação autônoma de visão computacional  
✅ **Critérios Cinemáticos**: Definição e calibração independentes  
✅ **Testes Práticos**: Condução e verificação pelos autores  

### 📋 Responsabilidade Integral

Os autores assumem **total responsabilidade** pelo conteúdo final, garantindo:
- ✓ Exatidão das análises
- ✓ Conformidade acadêmica
- ✓ Ausência de plágios
- ✓ Integridade técnica

---

## 📧 Contato e Suporte

- **Problemas técnicos?** Abra uma [Issue](https://github.com/seu-usuario/LAB-CV2026.2/issues)
- **Dúvidas?** Consulte a [página interativa](https://pahsantana.github.io/LAB-CV2026.2/)

---