# Inventário e Proveniência de Dados (`data/`)

Este diretório centraliza os recursos genômicos, modelos HMM e perfis transcriptômicos brutos utilizados nos capítulos analíticos da tese de doutorado de **Mariana Feitosa Cavalheiro**.

Devido ao grande volume de dados brutos e arquivos intermediários binários (genomas, leituras Illumina FASTQ, matrizes de anotação), o conteúdo desta pasta é des-rastreado do repositório Git via `.gitignore`. Este documento declara as fontes oficiais, acessos públicos e padrões de integridade para replicação integral.

---

## 1. Genomas de Referência e Anotações Estruturais (`data/genomes/`)

### 1.1. *Vellozia tubiflora* (Espécie Tolerante à Dessecação - DT)
- **Local:** `data/genomes/Vtub/`
- **Montagem:** Quase telômero-a-telômero (*near-T2T*), resolvida por haplótipos (PacBio HiFi + Hi-C, Haplotype A).
- **Arquivos Canônicos:**
  - `Vtub.hapA.v1.softmasked.fasta`: Sequência genômica montada (cromossomos nucleares pseudomoléculas 1A a 9A + plastoma e mitocôndria).
  - `Vtub.hapA.v1.softmasked.gff3`: Anotação estrutural gênica (EVM/BRAKER3 refinado).
  - `Vtub.hapA.v1.softmasked.cds.fasta`: Sequências codificadoras (CDS) dos transcritos canônicos.
  - `Vtub.hapA.v1.softmasked.proteins.fasta`: Proteoma deduzido canônico.
  - `vtub_master_annotation.tsv`: Anotação funcional integrada via EggNOG-mapper v2 / InterProScan.
- **Acesso Público:** NCBI BioProject PRJNAXXXXXX / Figshare DOI: `10.6084/m9.figshare.XXXXXX`.

### 1.2. *Vellozia peripherica* (Espécie Evitadora de Desidratação / Sempre-verde)
- **Local:** `data/genomes/Vper/`
- **Montagem:** Montagem a nível cromossômico (PacBio HiFi + Omni-C, Haplotype A).
- **Arquivos Canônicos:**
  - `Vper.hapA.v1.softmasked.fasta`: Sequência genômica montada (cromossomos nucleares 1A a 9A).
  - `Vper.hapA.v1.softmasked.gff3`: Anotação estrutural gênica.
  - `Vper.hapA.v1.softmasked.cds.fasta`: Sequências codificadoras canônicas.
  - `Vper.hapA.v1.softmasked.proteins.fasta`: Proteoma deduzido canônico.
  - `vper_master_annotation.tsv`: Anotação funcional integrada EggNOG-mapper v2.
- **Acesso Público:** NCBI BioProject PRJNAXXXXXX.

---

## 2. Táxons de Comparação e Grupos Externos (`data/references/` & `pipelines/02_macroevolution/00_data/`)

Para as análises filogenômicas, datação molecular (MCMCtree) e ganho/perda de famílias gênicas (CAFE5):

| Código | Espécie | Linhagem / Clado | Estratégia Hídrica | Fonte da Montagem / Proteoma |
| :--- | :--- | :--- | :--- | :--- |
| **Vtub** | *Vellozia tubiflora* | Velloziaceae focal | Tolerante à Dessecação (DT) | Este estudo (near-T2T) |
| **Vper** | *Vellozia peripherica*| Velloziaceae focal | Evitadora / Sempre-verde | Este estudo |
| **Xvis** | *Xerophyta viscosa* | Velloziaceae basal (África) | Tolerante à Dessecação (DT) | Costa et al. (2017) |
| **Abra** | *Acanthochlamys bracteata* | Velloziaceae basal (Ásia) | Tolerante à Dessecação (DT) | Yin et al. (2021) |
| **Ptec** | *Pandanus tectorius* | Pandanales (outgroup) | Mesófita | GigaDB / NCBI GCA_009804825.1 |
| **Dala** | *Dioscorea alata* | Dioscoreales (raiz 121.9 Ma) | Mesófita | Phytozome v13 |
| **Ath**  | *Arabidopsis thaliana*| Eudicotiledônea (QC anotação)| Mesófita | TAIR10 (usada para mapeamento GO) |

---

## 3. Dados Transcriptômicos RNA-Seq (`data/rnaseq/`)

Bibliotecas pareadas (paired-end Illumina NovaSeq 6000, 2x150 bp), coletadas em tecidos vegetativos sob irrigação controlada (três réplicas biológicas por tecido):

### *Vellozia peripherica* (`data/rnaseq/Vper/`)
- **Caule / Stem (C):** `VP1C`, `VP2C`, `VP3C`
- **Folha / Leaf (F):** `VP1F`, `VP2F`, `VP3F`
- **Raiz / Root (R):** `VP1R`, `VP2R`, `VP3R`

### *Vellozia tubiflora* (`data/rnaseq/Vtub/`)
- **Caule / Stem (C):** `VT1C`, `VT2C`, `VT3C`
- **Folha / Leaf (F):** `VT1F`, `VT2F`, `VT3F`
- **Raiz / Root (R):** `VT2R`, `VT3R` *(Nota de QC: A réplica `VT1R` foi excluída da análise final devido a falha estocástica de sequenciamento).*

---

## 4. Modelos HMM Pfam (`data/hmm/`)

Perfis de Modelos Ocultos de Markov obtidos do Pfam-A v35.0 para triagem e validação dos canais mecanossensíveis OSCA:
- **`PF02714.hmm`**: Domínio *RS_domain* (família TMEM63/OSCA).
- **`PF14703.hmm`** & **`PF13967.hmm`**: Domínios auxiliares estruturais e citoplasmáticos.

---

## 5. Validação de Integridade

Para verificar se os arquivos de dados locais correspondem exatamente aos dados utilizados nas análises:
```bash
sha256sum -c data/checksums.sha256
```
*(Um exemplo de formato de checksums está disponível em `data/checksums.sha256.example`).*

