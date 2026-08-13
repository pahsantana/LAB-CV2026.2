Aqui está o `README.md` atualizado com a adição do **Gemini** na Declaração do Uso de Inteligência Artificial Generativa, mantendo toda a estrutura de diretórios do ambiente:

# Projeto de Visão Computacional: Sistema de Detecção de Quedas de Idosos

Este repositório contém a documentação, os códigos de laboratório, os scripts do projeto final e as evidências de validação experimental com voluntários do **Sistema de Detecção e Classificação de Quedas**.

---

## 📁 Estrutura do Repositório (`LAB1_ENVIAR`)

```text
LAB1_ENVIAR/
├── lab1_arquivos/                  # Experimentos e atividades do Laboratório 1
├── lab2_arquivos/                  # Experimentos e atividades do Laboratório 2
├── lab3_arquivos/                  # Experimentos e atividades do Laboratório 3
├── lab4_arquivos/                  # Experimentos e atividades do Laboratório 4
├── lab5_arquivos/                  # Experimentos e atividades do Laboratório 5
├── lab6_arquivos/                  # Experimentos e atividades do Laboratório 6
├── lab7/                          # Experimentos e atividades do Laboratório 7
├── lab8_arquivos/                  # Experimentos e atividades do Laboratório 8
│
├── projeto/                        # Artefatos e datasets de apoio do projeto
│   ├── pics/                       # Imagens e registros fotográficos do dataset
│   └── refs/                       # Referências bibliográficas e documentos de apoio
│
├── teste_voluntarios/              # Validação prática com voluntários
│   ├── logs/                       # Registros de eventos gerados em tempo de execução
│   │   ├── log_detector_pessoas.csv
│   │   └── log_eventos_queda_otimizado.csv
│   ├── videos/                     # Registros em vídeo dos testes executados (.mp4)
│   │   ├── video_detector_pessoas.mp4
│   │   ├── video_detector_pessoas2.mp4
│   │   ├── video_detector_pessoas4.mp4
│   │   ├── video_detector_pessoas5.mp4
│   │   └── video_detector_pessoas7.mp4
│   └── teste-voluntarios-dados.ipynb  # Notebook de processamento e análise dos testes
│
├── artigo-grupo1-quedaidosos.pdf   # Artigo científico/relatório consolidado do grupo
├── index.html                      # Interface/página de apresentação interativa
├── roteiro_teste_detector_quedas.pdf # Roteiro metodológico aplicado aos testes
├── trabalho_final.ipynb            # Notebook principal do projeto (execução do pipeline)
└── README.md                       # Documentação principal do repositório

```

---

## ⚙️ Principais Artefatos do Projeto Final

* **`trabalho_final.ipynb`**: Notebook contendo o pipeline principal de Visão Computacional (aquisição, rastreamento via SSDLite320 MobileNetV3, cálculo cinemático e regras de decisão).


* **`teste_voluntarios/`**:
* **`logs/`**: Arquivos CSV com os registros de tempo, velocidade vertical, deslocamento e índice da escala SUS.


* **`videos/`**: Amostras gravadas durante os testes práticos de validação em laboratório.


* **`teste-voluntarios-dados.ipynb`**: Análise estatística dos logs e das métricas obtidas.




* **`artigo-grupo1-quedaidosos.pdf`**: Documentação formal do projeto em formato de artigo acadêmico.


* **`index.html`**: Painel web de apresentação com detalhes da solução, seminário e formulário de usabilidade (Escala SUS).



---

## 📜 Declaração de Integridade e Uso de IA Generativa (Portaria CNPq nº 2.664/2026)

Em cumprimento às diretrizes da Portaria CNPq nº 2.664/2026 sobre a transparência e integridade da pesquisa científica:

| Ferramenta de IAG | Fase do Desenvolvimento | Finalidade Específica |
| --- | --- | --- |
| **Claude** (*Anthropic*) | Desenvolvimento de Código | Apoio na estruturação, refatoração, sintaxe e otimização dos algoritmos em Python / Jupyter Notebook. |
| **Gemini** (*Google*) | Redação e Análise de Dados | Auxílio na síntese dos logs de execução, formulação de análises estatísticas, revisão técnica e padronização da documentação final. |

* **Autoria e Controle Humano:** Toda a concepção conceitual, arquitetura do modelo de visão computacional, coleta de dados e condução dos ensaios com voluntários foram idealizadas e executadas integralmente pelos autores, que assumem total responsabilidade pelo conteúdo final.

