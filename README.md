# Projeto de Visão Computacional: Sistema de Detecção e Classificação de Quedas em Idosos

Este repositório contém a documentação técnica completa, os módulos de aprendizado prático (Laboratórios 1 a 8), os scripts do projeto final e os registros de testes de usabilidade e validação com voluntários do **Sistema de Detecção e Classificação de Quedas em Tempo Real**.

---

## 📌 Sumário
1. [Estrutura do Repositório](#-estrutura-do-repositório-lab1_enviar)
2. [Conteúdo dos Laboratórios](#-conteúdo-dos-laboratórios-labs)
3. [Visão Geral do Projeto Final](#-visão-geral-do-projeto-final)
4. [Métricas e Resultados Experimental](#-métricas-e-resultados-experimentais)
5. [Instruções de Execução](#-instruções-de-execução)
6. [Declaração de IA Generativa (CNPq nº 2.664/2026)](#-declaração-de-integridade-e-uso-de-ia-generativa-portaria-cnpq-nº-26642026)

---

## 📁 Estrutura do Repositório (`LAB1_ENVIAR`)

```text
├── lab1_arquivos/                  # Lab 1: Fundamentos de Imagem, Espaços de Cor e Histogramas
├── lab2_arquivos/                  # Lab 2: Operações Ponto a Ponto e Filtragem Espacial
├── lab3_arquivos/                  # Lab 3: Detecção de Bordas, Gradientes e Transformada de Hough
├── lab4_arquivos/                  # Lab 4: Operações Morfológicas e Segmentação por Limiarização
├── lab5_arquivos/                  # Lab 5: Extração de Características (SIFT/ORB) e Contornos
├── lab6_arquivos/                  # Lab 6: Transformações Geométricas, Homografia e Calibração
├── lab7/                          # Lab 7: Fluxo Óptico, Rastreamento de Objetos e Análise de Movimento
├── lab8_arquivos/                  # Lab 8: Introdução a Redes Neurais Convolucionais e Detecção de Objetos
│
├── projeto/                        # Artefatos e datasets de apoio do projeto
│   ├── pics/                       # Imagens e registros fotográficos do dataset
│   └── refs/                       # Referências bibliográficas e documentos de apoio
│
├── teste_voluntarios/              # Validação prática com voluntários
│   ├── logs/                       # Registros cinemáticos e pontuações de eventos (.csv)
│   │   ├── log_detector_pessoas.csv
│   │   └── log_eventos_queda_otimizado.csv
│   ├── videos/                     # Registros em vídeo dos ensaios em tempo real (.mp4)
│   │   ├── video_detector_pessoas.mp4
│   │   ├── video_detector_pessoas2.mp4
│   │   ├── video_detector_pessoas4.mp4
│   │   ├── video_detector_pessoas5.mp4
│   │   └── video_detector_pessoas7.mp4
│   └── teste-voluntarios-dados.ipynb  # Notebook de processamento e análise estatística dos testes
│
├── artigo-grupo1-quedaidosos.pdf   # Artigo científico / relatório formal em PDF
├── index.html                      # Página/interface web de apresentação e formulários
├── roteiro_teste_detector_quedas.pdf # Roteiro metodológico aplicado aos testes de campo
├── trabalho_final.ipynb            # Notebook principal do projeto (pipeline completo)
└── README.md                       # Documentação principal do repositório

```

🛠️ Conteúdo dos Laboratórios (Labs)

lab1_arquivos/: Fundamentos de imagem digital, manipulação de matrizes de pixels, conversões de espaços de cores (RGB, HSV, Grayscale) e análise de histogramas
.lab2_arquivos/: Operações de filtragem espacial, convoluição 2D, redução de ruído (Blur, Gaussian, Median) e realce de bordas (Sharpening)
.lab3_arquivos/: Algoritmos de detecção de descontinuidades, operadores de Sobel, Laplaciano, Canny e extração de formas geométricas via Transformada de Hough
.lab4_arquivos/: Morfologia matemática (Erosão, Dilatação, Abertura e Fechamento) e técnicas de segmentação baseadas em limiarização simples, adaptativa e método de Otsu
.lab5_arquivos/: Identificação e pareamento de pontos de interesse (Keypoints), descritores invariantes a escala/rotação (SIFT/ORB) e hierarquia de contornos
.lab6_arquivos/: Transformações de perspectiva e afins, estimativa da matriz de homografia e calibração de câmeras para correção de distorções ópticas
.lab7/: Estimação de vetor de movimento por fluxo óptico denso/esparso (Lucas-Kanade, Farneback) e algoritmos de rastreamento de objetos
.lab8_arquivos/: Arquiteturas de Redes Neurais Convolucionais (CNNs) e modelos de detecção em tempo real, servindo de base para o pipeline do projeto final.

⚙️ Visão Geral do Projeto Final

O objetivo principal do projeto final é realizar a detecção automática de quedas de idosos em tempo real a partir de fluxos de vídeo convencionais (RGB), minimizando falsos positivos gerados por Atividades de Vida Diária (AVDs), como agachar ou sentar.Arquitetura da Solução:Rastreamento de Pessoas: Emprego da rede neural profunda SSDLite320 MobileNetV3 otimizada para execução local em CPU (Edge Processing).  Análise Cinemática: Extração do centroide e cálculo do vetor de velocidade vertical ($v$), deslocamento vertical ($\Delta y$) e variação da razão de aspecto ($w/h$) da bounding box.  Motor de Decisão Multicritério: Regra de pontuação acumulativa em janela temporal padronizada de $1,55\text{s}$ após a transição de postura (gatilho). O evento de queda é confirmado apenas se ao menos 3 dos 4 parâmetros cinemáticos atingirem os limiares críticos.  

📊 Métricas e Resultados Experimentais
Os ensaios práticos realizados no laboratório com voluntários demonstraram a eficácia do filtro multicritério:Parâmetro / MétricaLog Antigo / Legado (log_eventos_queda_otimizado.csv)Ensaios Intermediários de BancadaLog Atual de Vídeo (log_detector_pessoas.csv)Padrão de Transiçãoem_pe -> deitado  em_pe -> agachado  em_pe -> agachado -> em_pe e em_pe -> agachado  Janela Temporal ($t$)$\approx 0,18\text{s} - 0,20\text{s}$  $1,50\text{s} - 1,59\text{s}$  Padronizada em $1,55\text{s}$  Picos de Velocidade ($v$)$0,0\text{ px/s}$ a $-6,7\text{ px/s}$  $0,8\text{ px/s}$ a $5000,0\text{ px/s}$  Até $5500,0\text{ px/s}$  Confiança da Detecção
Não registrada  $0,71$ a $1,00$  $0,88$ a $0,99$ (SSDLite320)  Classificação Obtida
DEITOU_VOLUNTARIAMENTE  Flutuação entre QUEDA e NAO_QUEDA  EVENTO_NAO_CLASSIFICADO_COMO_QUEDA  Conclusão de Usabilidade: Em movimentos de agachamento rápido, picos isolados de velocidade ($5500,0\text{ px/s}$) foram descartados com sucesso (pontuação $2/4$), evitando falsos alarmes em AVDs.  🚀 Instruções de ExecuçãoPré-requisitos:Python 3.9+Jupyter Notebook / JupyterLabPacotes necessários: opencv-python, torch, torchvision, pandas, numpy, matplotlibExecução do Pipeline do Projeto:Bash# Clonar o repositório e acessar a pasta raiz

# Iniciar o Jupyter Notebook
jupyter notebook trabalho_final.ipynb
Análise dos Dados dos Voluntários:Abra o notebook teste_voluntarios/teste-voluntarios-dados.ipynb para visualizar a consolidação gráfica dos logs e métricas da Escala SUS. 

 📜 Declaração de Integridade e Uso de IA Generativa (Portaria CNPq nº 2.664/2026)
 
 Em cumprimento rigoroso às diretrizes da Portaria CNPq nº 2.664/2026 (Artigo 2º, alíneas c, d e f) sobre integridade acadêmica e transparência na pesquisa científica:Ferramenta de IAG
 Fase do Desenvolvimento
 Finalidade Específica
 Claude (Anthropic)Desenvolvimento de CódigoApoio na estruturação, refatoração, sintaxe e otimização dos algoritmos em Python / Jupyter Notebook.
 Gemini (Google)Redação e Análise de Dados
 Auxílio na síntese dos logs de execução, análises estatísticas, revisão técnica e padronização da documentação final em Markdown.Autoria e Controle Humano: Todo o escopo conceitual, a modelagem dos algoritmos de visão computacional, os critérios cinemáticos e a condução dos testes práticos foram concebidos, implementados e verificados autonomamente pelos autores.
 Responsabilidade Integral: Os autores assumem total responsabilidade pelo conteúdo final do trabalho, garantindo a exatidão das análises, a conformidade acadêmica e a ausência de plágios ou inconsistências técnicas.