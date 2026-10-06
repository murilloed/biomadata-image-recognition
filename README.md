# BiomaData — análise de imagens ambientais

Demonstração independente em Python do método de comparação temporal descrito no módulo de imagens do BiomaData. Usa somente imagens sintéticas geradas pelo exemplo. Não contém código, dados, documentos ou imagens institucionais da aplicação original.

## Objetivo e entrega

Comparar duas imagens já alinhadas da mesma área e destacar diferenças de luminância. Entrega percentual de células alteradas, diferença média, imagens de exemplo e relatório JSON.

## Técnicas e treinamento

Pillow converte as imagens para tons de cinza e reduz para uma grade 32 × 32. Um limiar identifica diferenças acima do valor configurado. Este baseline é determinístico: não treina uma rede neural nem utiliza MCTS, Policy/Value ou grafos para a comparação. Reconhecimento temático por machine learning é uma evolução futura.

## Executar

```bash
python -m pip install -e .
python -m biomavision.demo
python -m unittest discover -s tests -v
```

Os artefatos são gravados em `output/`. A função `biomavision.core.compare` também aceita imagens Pillow fornecidas pelo usuário, com dimensões iguais e alinhamento prévio.

## Limitações

Nuvens, iluminação, estação do ano e desalinhamento podem produzir diferenças sem mudança ambiental. O método não identifica automaticamente queimadas, não classifica uso do solo e não comprova ocupação irregular. Resultados exigem revisão humana. O exemplo não valida o funcionamento da aplicação institucional e não representa integração GIS; essa integração pertence ao módulo original.

## Evolução

Dados rotulados autorizados, divisão de treino/teste por território e período, modelos de classificação/segmentação e avaliação de erros por classe. Nenhuma métrica de reconhecimento treinado é atribuída a esta versão.

Código demonstrativo: licença MIT. As referências ao BiomaData contextualizam o estudo e não representam endosso institucional.
