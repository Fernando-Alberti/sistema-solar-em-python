Simulação 3D do Sistema Solar em Python

Este projeto implementa uma simulação 3D animada do Sistema Solar utilizando Python, mostrando os principais planetas orbitando o Sol. A visualização é gerada com Matplotlib em 3D e inclui animação do movimento orbital, estrelas no fundo e anéis para Saturno e Urano.


Funcionalidades:

Visualização 3D do Sistema Solar

Animação das órbitas dos planetas

Representação dos seguintes corpos celestes:

Mercúrio

Vênus

Terra

Marte

Júpiter

Saturno

Urano

Netuno

Plutão

Anel de Saturno

Anel inclinado de Urano

Fundo espacial com estrelas geradas aleatoriamente

Velocidades orbitais proporcionais aproximadas


Tecnologias utilizadas:

Python

NumPy

Matplotlib

Matplotlib Animation

Astroquery (JPL Horizons)


Instalação:

Clone o repositório:

git clone https://github.com/seu-usuario/simulacao-sistema-solar.git
cd simulacao-sistema-solar

Instale as dependências:

pip install numpy matplotlib astroquery


Como executar:

Execute o script Python;

python sistema_solar.py

Uma janela será aberta mostrando a simulação animada do Sistema Solar.


Como funciona:

O programa:

Importa bibliotecas científicas e de visualização.

Define os raios orbitais aproximados dos planetas em Unidades Astronômicas (UA).

Gera órbitas circulares usando funções trigonométricas.

Cria um gráfico 3D com Matplotlib.

Adiciona:

Sol no centro

planetas como pontos animados

órbitas

anéis planetários

estrelas aleatórias

Usa FuncAnimation para atualizar a posição dos planetas ao longo do tempo.


Estrutura da Simulação:
Corpo	Distância média do Sol (UA)
Mercúrio	0.39
Vênus	0.72
Terra	1.00
Marte	1.52
Júpiter	5.20
Saturno	9.58
Urano	19.18
Netuno	30.07
Plutão	39.48

As velocidades orbitais são ajustadas manualmente para manter proporções aproximadas entre os planetas.


Elementos visuais:

Sol: esfera amarela no centro

Planetas: pontos coloridos com tamanhos diferentes

Órbitas: círculos desenhados em 3D

Estrelas: pontos aleatórios no fundo

Anéis planetários: Saturno e Urano


Referências:

NASA JPL Horizons System

Matplotlib Documentation

Astroquery Documentation


Projeto desenvolvido para estudo de visualização científica, astronomia e programação em Python.
