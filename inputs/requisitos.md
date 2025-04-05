# Projeto: Data Warehouse de Empresas com Dados Públicos do CNPJ

## 🧩 Fontes de Dados
- Dados abertos da Receita Federal (CNPJ)
  - Disponível em: https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/
  - Formato: arquivos `.zip` contendo `.csv` e `.txt`
  - Frequência: Atualização mensal

## 🎯 Objetivos do Projeto
- Integrar e centralizar os dados das empresas brasileiras num único Data Warehouse
- Permitir análises por setor econômico, localização geográfica e situação cadastral
- Otimizar extração de estatísticas para políticas públicas e estudos de mercado

## 📦 Arquivos Relevantes para Ingestão
- `Empresas.csv`: CNPJ base, razão social, natureza jurídica
- `Estabelecimentos.csv`: CNPJ completo, endereço, CNAE, data de início
- `Socios.csv`: tipo de sócio, nome, qualificação
- `Simples.csv`: status no Simples Nacional
- `CNAE.csv`: tabela de classificação de atividades econômicas
- `Municipios.csv`: código e nome do município

## 📊 Métricas Desejadas
- Quantidade de empresas ativas por estado e setor (CNAE)
- Evolução do número de empresas ativas ao longo do tempo
- Distribuição por tipo de empresa (MEI, LTDA, SA)
- Participação de pessoas físicas vs jurídicas no quadro societário

## 💡 Regras e Observações
- Desconsiderar registros com situação cadastral "baixada"
- Tratar CNPJs com dados incompletos (campos nulos ou inconsistentes)
- Cruzar informações dos estabelecimentos com os dados dos sócios

## 📂 Outputs Esperados
- Modelo lógico contendo tabelas normalizadas com relacionamentos
- Pipeline de ingestão (ETL/ELT) inicial
- Infraestrutura proposta com ferramentas Open Source
- Documento de validação final atestando conformidade com os requisitos
