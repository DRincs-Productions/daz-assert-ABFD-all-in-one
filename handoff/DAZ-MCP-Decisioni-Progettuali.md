# Handoff — decisioni per DAZ MCP e workflow scene

> Documento di lavoro incrementale. Raccoglie le decisioni concordate con l'utente; **non è ancora il piano operativo definitivo per Codex**. Aggiornare questo file quando vengono prese nuove decisioni, distinguendo decisioni confermate, proposte e questioni aperte.

## Repository e organizzazione — decisioni confermate

- Progetto principale: `DRincs-Productions/daz-assert-ABFD-all-in-one`.
- Repository autonomo per le estensioni: `DRincs-Productions/daz-mcp` (`https://github.com/DRincs-Productions/daz-mcp`).
- **Da fare, non ancora eseguito:** aggiungere `daz-mcp` al progetto principale come **Git submodule**.
- `daz-mcp` estende le capacità MCP di DAZ Studio senza sostituire né duplicare inutilmente il server upstream `bluemoonfoundry/daz-mcp-server`, già presente come submodule `mcp-server` nel progetto principale.
- L'ambito di `daz-mcp` è generale (non solo posing): strumenti MCP e Skill per DAZ Studio.
- Codex, durante lo sviluppo, dovrà mantenere aggiornati README, Skill e documentazione tecnica **all'interno del repository `daz-mcp`**. Le modifiche al submodule si committano nel suo repository; successivamente si aggiorna il puntatore del submodule nel progetto principale.
- Le procedure generali delle scene appartengono alla documentazione del progetto principale, nel submodule `docs/` (Wiki Git); non vanno duplicate in `daz-mcp`.

## Obiettivi dell'analisi locale — decisioni confermate

- L'utente fornirà immagini di riferimento, generalmente con **1–3 personaggi**, non grandi gruppi.
- Il valore aggiunto dell'AI locale è l'**estrazione di dati geometrici**, non la descrizione verbale di contenuti che Codex sa già interpretare.
- **Human pose estimation:** rilevare per ogni personaggio keypoint/articolazioni 2D e stimare lo scheletro 3D, orientamenti e dati utili al retargeting su **Genesis 9**; gestire sovrapposizioni e punti nascosti indicando l'incertezza.
- **Camera estimation/calibration:** stimare, rispetto ai personaggi, angolazione, posizione relativa, altezza, inclinazione, distanza relativa, inquadratura, campo visivo e focale dove possibile.
- Considerare la **calibrazione congiunta posa-camera**, anche attraverso proiezione delle articolazioni nella camera DAZ e confronto con i punti dell'immagine.
- Non trattare distanza assoluta, profondità o focale ricavate da una singola immagine come valori certi: possono essere intrinsecamente ambigui.
- I calcoli pesanti devono avvenire **localmente** e sfruttare la GPU quando disponibile; mantenere **basso il consumo di token Codex** attraverso strumenti MCP ad alto livello e output sintetici. Dati estesi su file quando necessario.

## Ruoli di Codex e strumenti — decisioni confermate

- **Codex mantiene l'autonomia** di comprendere la scena DAZ, riconoscere oggetti/superfici (es. letto), decidere dove collocare i personaggi, scegliere asset e pose iniziali e organizzare la scena. L'utente ha già verificato che Codex sa individuare autonomamente il letto e posizionarvi un personaggio.
- Gli strumenti locali forniscono dati scheletrici, stime della camera, retargeting, calibrazione e operazioni ripetitive; non devono sostituire il ragionamento contestuale di Codex.
- Conservare il workflow esistente: cercare e mostrare una posa candidata, applicare posa approssimativa, collocare il personaggio, regolare camera, quindi rifinire e verificare.
- Per le verifiche intermedie preferire screenshot del viewport; non effettuare render Iray intermedi.

## Camera e procedura di scena — decisioni confermate

- **Da documentare** nella procedura di creazione/completamento scene `docs/Procedure-Scene-Posing-Completion.md`: Codex deve impostare anche **Focal Length**, posizione, rotazione, distanza/inquadratura, FOV e gli altri parametri pertinenti della camera, non soltanto puntarla verso il personaggio.
- Il modulo locale può suggerire stime; Codex applica e verifica la camera rispetto alla reference.
- Aggiornare la procedura nel submodule `docs/` con il corretto workflow Git; questa modifica non è ancora stata eseguita.
- Prima dell'implementazione Codex dovrà leggere integralmente la procedura reale. Il suo contenuto **non è stato ancora verificato integralmente in questa conversazione**.

## Tecnologie da valutare — proposte, NON scelte obbligatorie

Codex è libero di valutare, combinare, sostituire o scartare i seguenti candidati e di individuare alternative migliori:

- SAM 3D Body — ricostruzione 3D del corpo da immagine: `https://github.com/facebookresearch/sam-3d-body`.
- Multi-HMR 2 — ricostruzione multi-persona: `https://github.com/naver/multi-hmr2`.
- MMPose / RTMPose — keypoint e scheletro 2D: `https://github.com/open-mmlab/mmpose`.
- VGGT — stima geometrica/prospettica e camera: `https://github.com/facebookresearch/vggt`.
- OpenCV — calibrazione, proiezione e ottimizzazione geometrica: `https://opencv.org/`.
- Python è candidato preferenziale per AI locale/GPU; DAZ Script/JavaScript è utile per interagire con DAZ Studio. L'architettura definitiva spetta a Codex.

**Criteri di scelta:** qualità sulle immagini reali dell'utente, multi-persona, ricostruzione 3D, stima camera, integrazione Genesis 9, velocità, VRAM, compatibilità, licenze, manutenzione e facilità di installazione.

## Hardware — da verificare

- GPU dell'utente **indicativamente** NVIDIA RTX 4090 con 24 GB VRAM; il modello non è confermato.
- Codex dovrà rilevare la GPU effettiva prima di decidere modelli, versioni CUDA e requisiti.

## Vincoli del progetto principale da rispettare

- Prima di avviare o usare server MCP per il progetto principale, seguire le regole di `AGENTS.md` sulla disponibilità locale dei file richiesti, inclusi submodule e Git LFS.
- Per gli asset DAZ, usare i percorsi effettivi del content manager sotto DAZ Studio Formats, senza indovinarli.
- Mantenere separati esperimenti/calibrazioni e salvataggi definitivi della scena.
- Conservare screenshot temporanei fuori dal repository, secondo le convenzioni del progetto.
- Rispettare le procedure della Wiki per rendering finale e gestione scene.

## Stato e prossimi aggiornamenti

- Questo documento è un **handoff delle decisioni**, non un'autorizzazione a implementare subito tutte le funzionalità.
- **Non ancora eseguiti:** aggiunta del submodule `daz-mcp`, implementazione dei moduli AI, modifica delle procedure Wiki.
- **Da definire insieme:** interfacce MCP, criteri di accuratezza, formato dei dati scheletrici, test con reference reali, ordine delle implementazioni.
- Il Markdown operativo definitivo per Codex sarà preparato **solo al termine della fase decisionale**, su richiesta dell'utente.

## Registro decisioni

| Data | Stato | Decisione |
| --- | --- | --- |
| 2026-10-28 | Confermata | `daz-mcp` sarà un submodule autonomo; README/Skill nel suo repository. |
| 2026-10-28 | Confermata | Analisi locale di scheletri 2D/3D e geometria camera da reference con 1–3 persone. |
| 2026-10-28 | Confermata | Codex mantiene autonomia nel posizionamento dei personaggi e nell'interpretazione della scena. |
| 2026-10-28 | Confermata | Aggiornare la procedura di scena per focale e impostazioni complete della camera. |
| 2026-10-28 | Confermata | Codex sceglierà liberamente i modelli AI dopo valutazione, senza vincoli sulle librerie suggerite. |

## Dati generati dal MCP — decisione confermata

- **Non committare nel progetto principale** gli output generati dal MCP durante l'analisi delle scene: scheletri/keypoint 2D e 3D, stime e calibrazioni della camera, risultati di ottimizzazione, cache dei modelli, log e dati intermedi.
- Prevedere una directory locale dedicata e **ignorata da Git**, proposta: `/.daz-mcp-cache/` nella root del progetto principale, con sottocartelle per scena o task e nomi stabili quando utili. Il percorso esatto potrà essere valutato da Codex, purché resti escluso dal versionamento.
- Codex dovrà aggiungere la directory a `.gitignore` durante l'implementazione e verificare che nessun output venga tracciato. Non ignorare indiscriminatamente file sorgente, procedure, Skill o asset deliberatamente versionati.
- Distinguere i dati intermedi dagli eventuali **artefatti finali esplicitamente richiesti dall'utente**, per i quali valgono le convenzioni di salvataggio del progetto.
- Conservare la regola esistente sugli screenshot del viewport: file temporanei in `%TEMP%/DAZ-Scene-Previews/`, fuori dal repository; non spostarli automaticamente nella nuova cache.
- La directory ignorata e la modifica di `.gitignore` sono **da realizzare in seguito**; qui si registra soltanto la decisione.

| 2026-10-28 | Confermata | Gli output di analisi del MCP devono restare in una cartella locale ignorata da Git, separati dal codice versionato. |

## Camera Live View e osservazione a basso costo — decisione confermata (requisito)

- Prevedere in `daz-mcp` strumenti MCP per **elencare le camere DAZ**, scegliere quella da osservare e ottenere il relativo viewport senza dover eseguire render Iray intermedi.
- Distinguere **anteprima live locale** (eventuale finestra/pannello/stream sul PC, senza inviare continuamente frame a Codex) e **osservazione per Codex** (snapshot su richiesta, campionamento controllato e/o risultati di analisi locale sintetici).
- Obiettivo: minimizzare consumo di token/crediti e traffico di immagini verso Codex; niente stream continuo di frame nel contesto del modello.
- Prevedere selezione di una camera specifica, passaggio tra camere e possibilità di confrontare la vista con la reference. Verificare tecnicamente se sia possibile catturare viste di camere non attive senza alterare la selezione corrente; in caso contrario gestire ripristino sicuro dello stato.
- La modalità di preview, la frequenza di aggiornamento, i metodi di cattura e l'interfaccia locale sono **da valutare e implementare da Codex**, senza assumere API DAZ non verificate.
- Conservare le convenzioni esistenti sugli screenshot temporanei fuori dal repository e non committare i frame/cache generati.

| 2026-10-28 | Confermata | Camera Live View locale selezionabile, con snapshot/analisi su richiesta per Codex e minimo consumo di token. |
