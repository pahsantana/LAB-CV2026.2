# LAB-CV2026.2 — Visão Computacional Aplicada

Repositório destinado ao desenvolvimento das atividades práticas e do projeto final da disciplina **ESZA019 - Visão Computacional**.

---

## 🚀 Projeto Final

### **Sistema Inteligente de Monitoramento e Aviso de Queda de Idosos Doméstico e em ILPIs**
O projeto consiste em um sistema de visão computacional voltado para a segurança na terceira idade. Através do processamento de imagens de câmeras locais e algoritmos geométricos/cinemáticos baseados em *Edge Computing*, o sistema identifica quedas em tempo real, preservando totalmente a privacidade e a identidade dos usuários.

* 🔗 **[CLIQUE AQUI PARA ACESSAR A PÁGINA INTERATIVA DO PROJETO](https://pahsantana.github.io/LAB-CV2026.2/)**

---

## 📊 Relatório de Resultados e Validação com Voluntários (Etapa 7: Seminário)

### 1. Matriz Completa de Avaliação e Feedback

A tabela a seguir unifica os enunciados das 17 questões aplicadas no formulário, reunindo as pontuações individuais de usabilidade (Q1 a Q11), as médias ponderadas, percentuais de favorabilidade e o registro textual dos testes conduzidos com os 7 voluntários:

| Avaliador | 1. Gostaria de usar esse sistema com frequência | 2. Achei o sistema desnecessariamente complexo | 3. Achei o sistema fácil de usar | 4. Acho que precisaria de suporte de uma pessoa técnica para usar esse sistema | 5. Achei que várias funções do sistema foram bem integradas | 6. Achei que havia várias inconsistências no sistema | 7. Imagino que a maioria das pessoas aprenderia a usar esse sistema rapidamente | 8. Achei o sistema complicado de usar | 9. Me senti confiante ao usar o sistema | 10. Precisei aprender muitas coisas antes que pudesse usar o sistema | 11. Você achou o sistema interativo? | 12. Do que você mais gostou no sistema? | 13. Do que você menos gostou no sistema? | 14. Sugestões e comentários | 15. Qual é o objetivo deste sistema testado? | 16. Descreva resumidamente os experimentos | 17. Resultados obtidos |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **José Victor C. de Carvalho** | 5 | 1 | 5 | 2 | 5 | 2 | 5 | 2 | 5 | 2 | 5 | Gostei de como implementaram. | Nada em específico. | Nada em específico. | O objetivo é reconhecer quedas bruscas. | Eu simulei uma queda na frente da câmera e o sistema identificou a queda. | O sistema identificou minha queda e reportou os metadados da queda. |
| **Antônio Carlos F. Vidal Jr.** | 5 | 1 | 4 | 1 | 5 | 1 | 5 | 1 | 4 | 1 | 3 | Aplicabilidade. | Qualidade câmera. | Implementação de um feedback ao vivo. | Detectar quedas. | Implementei movimentações pré-definidas e estudei o sistema. | Resultado se estava em pé, agachado ou caído. |
| **Vinícius de Morandi Costa** | 5 | 1 | 5 | 2 | 5 | 1 | 5 | 1 | 5 | 1 | 5 | A utilidade para fins de saúde pública. | Que ainda não está completamente disponível. | Lançar o quanto antes. | Identificar a queda de pessoas que não têm vulnerabilidade. | Eu me afastei um pouco à câmera e agachei. O sistema me mostrou que eu havia abaixado. | *Não preenchido* |
| **Rafael S. Coelho** | 5 | 1 | 5 | 3 | 5 | 1 | 5 | 1 | 4 | 1 | 3 | Detectar a queda. | Eu preciso cair no processo. | Alarme de queda. | Verificar uma possível queda. | Me agachei, o sistema detectou e em seguida me joguei no chão. | O sistema identificou bem o agachamento e queda. |
| **Ricardo de Andrade** | 5 | 1 | 5 | 1 | 3 | 2 | 5 | 1 | 4 | 1 | 4 | A ideia do projeto é muito interessante. | Faltou detectar mais de 1 usuário. | Detecção de mais pessoas; ampliação do range de detecção da câmera. | Detectar acidentes de pessoas em situações de queda. | Detecção em pé e agachado de um usuário; Tentativa de detecção de mais usuários. | Foi detectada 1 queda de usuário. |
| **Leandro Fernandes Reucci** | 5 | 1 | 5 | 1 | 5 | 1 | 5 | 1 | 4 | 1 | 5 | Que seja possível detectar rápido a queda. | *Não preenchido* | *Não preenchido* | Verificar se houve uma queda. | Em princípio fiquei de pé, depois fiquei agachado e por fim me joguei no chão. | Ele verificou e classificou corretamente os três poses. |
| **Samira Harada** | 5 | 1 | 5 | 1 | 5 | 1 | 5 | 1 | 4 | 1 | 5 | Tem um impacto muito grande. | Andar a cadeira e a execução. | Inclusão de interface amigável + sistema de alerta de queda (SMS, alarme, etc.). | Detectar quedas. | Fingi uma queda e averiguei que o sistema detectou minha queda. | A queda foi detectada. |
| **Média Ponderada** | **5,00** | **1,00** | **4,86** | **1,57** | **4,71** | **1,29** | **5,00** | **1,14** | **4,29** | **1,14** | **4,29** | — | — | — | — | — | — |
| **Favorabilidade (%)** | **100,0%** | **100,0%** | **100,0%** | **85,7%** | **85,7%** | **100,0%** | **100,0%** | **100,0%** | **100,0%** | **100,0%** | **71,4%** | — | — | — | — | — | — |

---

### 2. Avaliação de Usabilidade e Satisfação do Usuário (SUS)

Para avaliar a usabilidade de forma padronizada, aplicamos a metodologia internacional **SUS (System Usability Scale)** nas dez primeiras perguntas do formulário. O sistema alcançou uma pontuação média de **94,29 de 100 pontos**, o que o coloca no nível **A+ (Excelente)**, bem acima do ponto de corte de 80,3 considerado referência de mercado.

Individualmente, as notas do SUS variaram de 90,0 a 97,5 pontos (José Victor: 90,0; Antônio Carlos: 95,0; Vinícius: 97,5; Rafael: 92,5; Ricardo: 90,0; Leandro: 97,5; Samira: 97,5).

Analisando o conjunto das perguntas 1 a 11, **94,8% de todas as respostas foram estritamente favoráveis** à facilidade de uso do software. As respostas neutras representaram apenas 5,2% da amostra, concentrando-se pontualmente em dúvidas sobre necessidade de suporte (Q4), integração (Q5) e interatividade (Q11). Não houve nenhuma resposta desfavorável registrada, resultando em uma taxa de rejeição de 0,0%.

---

### 3. Análise Técnica dos Resultados e Próximos Passos

No aspecto técnico, o detector utiliza o modelo **SSDLite320 MobileNetV3** processando o rastreamento em tempo real direto na CPU. Durante a janela de análise de 1,5 segundo, a aplicação monitora quatro variáveis principais: tempo, deslocamento vertical, velocidade e a razão entre largura e altura ($L/A$). Nos testes práticos, o sistema registrou picos de velocidade de até $5500\text{ px/s}$ com tempo de resposta em $1,55\text{s}$, validando a eficiência da abordagem.

O retorno dos voluntários confirmou o apelo prático da solução, especialmente pela aplicação na saúde pública e prevenção de acidentes. Para as próximas etapas, os pontos centrais de evolução incluem criar um sistema ativo de alertas (via SMS ou sinal sonoro), estender a detecção para múltiplos usuários no mesmo quadro, ampliar o ângulo da câmera e ajustar as regras de decisão para evitar falsos alarmes em movimentações mais bruscas.

---

## 📂 Organização do Repositório

O repositório está estruturado para contemplar a proposta, os scripts de execução, o relatório de testes e as validações do projeto principal, além dos laboratórios práticos da disciplina:

### 🛠️ Projeto Final & Arquivos da Raiz
* 📁 **[`/projeto`](./projeto/)** — Diretório contendo os assets, componentes e arquivos complementares da página e do sistema do projeto final.
* 📁 **[`/teste_voluntarios`](./teste_voluntarios/)** — Pasta contendo os relatórios de testes, gravações de vídeo (`video_detector_pessoas.mp4` a `video_detector_pessoas7.mp4`) e o notebook de processamento estatístico `teste-voluntarios-dados.ipynb`.
* 📄 **[`trabalho_final.ipynb`](./trabalho_final.ipynb)** — Notebook principal com a implementação, pipeline de inferência e testes do detector de quedas.
* 📄 **[`roteiro_teste_detector_quedas.pdf`](./roteiro_teste_detector_quedas.pdf)** — Documentação do protocolo experimental e cenários de testes validados.
* 🌐 **[`index.html`](./index.html)** — Interface web interativa apresentando a proposta, estudo de empatia, arquitetura e métricas do projeto.

---

### 🧪 Índice de Atividades Práticas (Laboratórios)
* 📁 **[Laboratório 01](./lab1_arquivos/)** — Captura de Imagem e Vídeo
* 📁 **[Laboratório 02](./lab2_arquivos/)** — Extração de Características (*Features*)
* 📁 **[Laboratório 03](./lab3_arquivos/)** — Alinhamento, Homografia 2D e Mosaico
* 📁 **[Laboratório 04](./lab4_arquivos/)** — Calibração de Câmeras
* 📁 **[Laboratório 05](./lab5_arquivos/)** — Câmera Estéreo
* 📁 **[Laboratório 06](./lab6_arquivos/)** — *Depth Map* (Mapa de Profundidade)
* 📁 **[Laboratório 07](./lab7/)** — Introdução às Redes CNN (*Convolutional Neural Network*)
* 📁 **[Laboratório 08](./lab8_arquivos/)** — Rastreamento de Objetos

---

## 👥 Integrantes do Grupo

* **Eduarda Alexandre de Salles** — RA: 11202320551
* **Gustavo de Paula Souza** — RA: 11202130568
* **Paloma Cristina Santana** — RA: 11201921396