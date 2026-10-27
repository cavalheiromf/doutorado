# Doutorado — genômica e história evolutiva de Velloziaceae

Repositório de Mariana Feitosa Cavalheiro, Universidade Estadual de Campinas. O enquadramento da tese reúne formação computacional, recursos genômicos e análises comparativas para apoiar investigações de respostas à limitação hídrica em Velloziaceae.

## Onde começar

| Trabalho | Entrada principal |
|---|---|
| Escrita, revisão e apresentações | [teamwork](teamwork/README.md) |
| Macroevolução: manuscritos e comunicação | [Área de trabalho](teamwork/chapters/macroevolution/README.md) |
| Macroevolução: resultados atuais | [CURRENT_OUTPUTS](chapter_macroevolution/04_gene_families/CURRENT_OUTPUTS.md) |
| OSCA: manuscrito e tabelas suplementares | [Manuscrito](chapter2_osca/manuscript/chapter_2_osca_mechanosensation.md) |
| OSCA: revisão dos resultados | [Auditoria](chapter2_osca/audits/relatorio_auditoria_capitulo2.md) |
| Visão operacional do repositório | [PROJECT](PROJECT.md) |

## Função das pastas

- `data/`: dados de referência compartilhados; manter caminhos usados pelos pipelines.
- `chapter_macroevolution/`: ortologia, filogenômica, datação, famílias gênicas, Ka/Ks e seus produtos analíticos.
- `chapter2_osca/`: projeto temático OSCA, com identificação, filogenia, sintenia, taxas, promotores, RNA-seq, expressão e redes.
- `teamwork/chapters/`: manuscritos, revisões, slides e arquivo histórico por tema.
- `teamwork/shared/`: literatura, revisões transversais, matrizes e bibliografias.
- `docs/`: documentação institucional e qualificação; os demais materiais foram distribuídos no teamwork, com links nos caminhos anteriores.
- `logs/`: registros de execução; `reports/` é um link para documentos OSCA centralizados em `teamwork/chapters/osca/reviews/root_reports/`, ainda sem nova validação científica.

Os nomes chapter1/chapter2 de arquivos antigos não definem a numeração atual da tese. Os projetos de macroevolução e OSCA são áreas temáticas; este repositório não foi inventariado como contendo integralmente os quatro capítulos descritos na Introdução.

## Resultados e limites

Na macroevolução, a referência atual contém 196 famílias de consenso entre modelos e 58 adicionais apoiadas por k=3. As análises de Ka/Ks de referência são descritivas; razões ω > 1 não equivalem a confirmação estatística de seleção positiva. A comparação evolutiva oferece uma base para investigar possíveis relações com respostas à seca e à dessecação.

Os relatórios de auditoria OSCA e os índices de macroevolução têm precedência sobre planos antigos com números substituídos. Uma figura ou relatório de QA visual não valida sozinho as inferências científicas.

## Organização e reprodução

Dados e resultados volumosos permanecem junto aos pipelines. A área de escrita usa `manuscripts`, `reviews`, `slides` e `archive`. Os caminhos antigos preservados como links não são cópias adicionais; consultar teamwork para os caminhos principais.

Antes de reproduzir uma análise, conferir o script, ambiente, dados e execução de referência do módulo. Não há um comando único validado para reexecutar todo o repositório. As reorganizações não reexecutaram análises ou converteram rascunhos em resultados finais.

O [README anterior](teamwork/shared/evidence_matrices/README_repository_before_2026-10-05.md) está preservado para rastreabilidade.

Para uma navegação com menos caminhos duplicados no VS Code, abrir [doutorado.code-workspace](doutorado.code-workspace). Esse workspace oculta apenas os acessos de compatibilidade indicados e mantém os arquivos disponíveis; não altera as configurações atuais do editor.
