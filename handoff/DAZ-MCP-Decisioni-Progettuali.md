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

## Monitor multicamera esterno e vista libera — requisiti confermati

- Il modulo Camera Live View deve prevedere una **finestra esterna dedicata**, capace di mostrare **più camere DAZ contemporaneamente**, oltre a una **vista libera di ispezione**.
- La vista libera ("camera dell'utente" / prospettiva di navigazione) deve poter essere spostata e ruotata autonomamente, con zoom su dettagli, articolazioni, contatti e oggetti. Non deve alterare involontariamente posizione, rotazione, focale o altre impostazioni delle camere di produzione.
- Codex deve poter scegliere quale vista osservare, muovere la vista libera e richiedere snapshot mirati; la visualizzazione live locale non deve inviare continuamente frame al contesto di Codex.
- Codex dovrà verificare API, prestazioni e fattibilità della cattura simultanea di più viste in DAZ Studio; l'implementazione tecnica non è stata scelta.
- Le immagini/cache prodotte restano fuori dai commit e rispettano le convenzioni di storage temporaneo del progetto.

## Validatore Genesis 9 esistente — valutazione e migrazione proposta

- File esistente nel repository principale: `validate_genesis9_rig.py` (letto il 2026-10-28).
- Il file valida **strutturalmente** un JSON di cattura del rig Genesis 9: schema 1.0, nome figura, elenco e ID delle ossa, coordinate locali/world, canali di rotazione, relazioni padre-figlio, gruppi ossei essenziali e flag di cattura read-only. **Non** stima pose da immagini né certifica la correttezza del sistema di coordinate.
- **Proposta da sottoporre a Codex:** valutare riuso/refactoring di questa logica dentro `daz-mcp` come servizio/strumento MCP di validazione rig, mantenendo test di regressione.
- Prima di eliminare lo script originale, Codex dovrà cercare tutte le dipendenze/riferimenti nel progetto e nelle procedure, garantire la parità funzionale e aggiornare la documentazione. **Nessuna rimozione autorizzata o eseguita ora.**

| 2026-10-28 | Confermata | Finestra esterna multicamera con vista libera navigabile e zoom indipendente dalle camere di produzione. |
| 2026-10-28 | Proposta da valutare | Riutilizzare in `daz-mcp` il validatore `validate_genesis9_rig.py`, rimuovendo l'originale solo dopo verifica delle dipendenze e dei test. |

## Dashboard multicamera via browser — proposta tecnica da valutare

- È **fattibile in linea di principio** una dashboard locale in Chrome/Chromium o altro programma, collegata a DAZ Studio tramite un servizio locale che distribuisce le anteprime delle camere.
- Distinguere chiaramente tre livelli: DAZ produce/cattura le viste; il servizio locale le trasmette e riceve comandi; il browser mostra più camere e la vista libera, con navigazione/zoom.
- Chrome DevTools MCP è un **candidato facoltativo** per permettere a Codex di controllare/ispezionare la pagina web; **non** produce da solo le immagini 3D di DAZ. Evitare di obbligare Codex a usare il browser per ogni operazione della camera quando sono disponibili API MCP DAZ dirette.
- Le API DAZ documentano `Dz3DViewport.captureImage()`, `setCamera()` e gestione di più viewport tramite `DzViewportMgr`; questo **non dimostra ancora** che la cattura simultanea continua di tutte le camere sia efficiente o fattibile nella configurazione specifica. Codex dovrà prototipare e misurare aggiornamento, latenza e impatto sulle prestazioni.
- Privilegiare stream locale/aggiornamenti differenziali o snapshot su richiesta, senza inviare frame continui al modello. Non introdurre render Iray intermedi.
- La scelta browser vs applicazione desktop e la tecnologia di trasmissione restano **aperte** e saranno decise da Codex in base ai test.

| 2026-10-28 | Proposta da valutare | Dashboard multicamera in Chrome/Chromium tramite servizio locale DAZ; Chrome DevTools MCP opzionale, non sostitutivo del backend DAZ. |

## Acquisizione e consegna automatica delle camere di scena — decisione confermata

- Aggiungere al modulo Camera Live View un'**operazione MCP unica, attivabile su richiesta**, che individui tutte le camere di scena e produca **un'immagine distinta per ciascuna**, **escludendo la vista/camera di lavoro** usata per navigare e ispezionare.
- L'esclusione della camera di lavoro deve essere affidabile: distinguere esplicitamente la vista libera dalle camere di produzione, senza assumere che la camera attiva sia sempre quella di lavoro.
- Le immagini devono essere etichettate con nome/identificativo della camera e rese disponibili per **l'invio all'utente come immagini separate**, evitando che Codex debba eseguire manualmente una cattura e un invio per ogni camera.
- Codex dovrà verificare le capacità effettive del client MCP/Codex per allegare o mostrare automaticamente più immagini: se l'invio diretto non è supportato, prevedere un flusso alternativo con minimo intervento, senza promettere consegne impossibili.
- Evitare render Iray intermedi, preservare stato delle camere e viewport, minimizzare chiamate e token; la funzione è **on demand**, non uno stream continuo verso Codex.
- I file temporanei devono seguire le convenzioni del progetto ed essere esclusi dai commit Git.

| 2026-10-28 | Confermata | Un comando MCP deve acquisire e predisporre l'invio separato delle immagini di tutte le camere di scena, escludendo la vista di lavoro. |

## Funzionalità avanzate del modulo camere — decisioni confermate

Integrare nel progetto `daz-mcp`, riutilizzando ove possibile funzionalità esistenti, tutte le seguenti capacità:

1. **Confronto automatico reference/viewport**: confronto locale tra immagine di riferimento e camera DAZ con metriche strutturate di allineamento, keypoint, scala, composizione e confidenza; evitare invii ripetuti di screenshot al modello.
2. **Inquadratura automatica**: adattare camera e margini a uno o più personaggi/oggetti selezionati, senza perdere impostazioni importanti.
3. **Navigazione mirata della vista libera**: centrare/orbitare/zoomare su articolazioni, volto, mani, piedi, punti di contatto o altri elementi selezionati; preservare le camere di produzione.
4. **Overlay scheletro**: visualizzare sulle viste DAZ i keypoint/scheletri estratti dalla reference e/o quelli proiettati dal rig DAZ, distinguendoli chiaramente.
5. **Snapshot e ripristino camera**: salvare e recuperare posizione, rotazione, focal length e parametri rilevanti, con ripristino sicuro dopo tentativi di calibrazione.
6. **Validazione automatica inquadrature**: segnalare personaggi tagliati, soggetti troppo piccoli, occlusioni rilevanti, direzione errata e altri problemi verificabili; non presentare euristiche come certezze.
7. **Ottimizzazione locale della camera rispetto alla reference**: effettuare tentativi e valutazioni localmente, con metriche e limiti, restituendo a Codex la configurazione migliore; distinguere gli errori di posa da quelli di camera e consentire a Codex di approvare/applicare o ripristinare.

Queste sono **capacità richieste**, non vincoli sull'architettura o sulla scelta di librerie. Codex dovrà verificarne fattibilità, prestazioni, integrazione con l'MCP upstream e comportamento reale in DAZ Studio, evitando duplicazioni e consumo superfluo di token.

## Aggiornamento continuo delle procedure Markdown — decisione confermata

- Durante lo sviluppo, ogni modifica significativa o nuovo strumento MCP deve comportare la revisione delle procedure Markdown pertinenti, in particolare `docs/Procedure-Scene-Posing-Completion.md` nel submodule Wiki `docs/`.
- Integrare i nuovi strumenti nei workflow effettivi (camera, posa, verifica, screenshot, ottimizzazione), migliorare i processi in generale ed eliminare istruzioni obsolete o ridondanti quando la sostituzione è verificata.
- Aggiornare anche README, Skills e documentazione tecnica nel repository `daz-mcp` quando appropriato.
- Modificare e committare i file nel repository/submodule proprietario corretto e aggiornare i gitlink del progetto principale. Non affermare che una procedura è verificata prima di averla testata.

## Test reali durante lo sviluppo — decisione confermata

- Codex deve **aprire DAZ Studio e testare concretamente** le funzionalità sviluppate con il server MCP, scene e camere pertinenti; i soli test unitari/statici non bastano.
- Verificare comportamento reale, qualità dell'inquadratura, selezione e ripristino delle camere, isolamento della vista libera, funzionamento multicamera, output delle immagini e assenza di modifiche involontarie alla scena.
- Eseguire test incrementali dopo modifiche rilevanti, riportare esito, limiti e problemi; non dichiarare completata una funzione non testata in DAZ.
- Rispettare le regole del progetto per anteprime viewport, nessun render Iray intermedio e nessun file temporaneo committato.
- La parola «fax» nel messaggio utente è interpretata **provvisoriamente come «DAZ»**; chiedere conferma se il significato è diverso.

| 2026-10-28 | Confermata | Tutte le sette funzionalità avanzate di camera, inclusa ottimizzazione locale rispetto alla reference. |
| 2026-10-28 | Confermata | Aggiornamento continuo delle procedure MD e dei workflow durante lo sviluppo. |
| 2026-10-28 | Confermata | Apertura di DAZ Studio e test funzionali reali durante lo sviluppo. |

## Scene Inspector & Spatial Intelligence — progettazione approvata

Realizzare in `daz-mcp` un modulo di analisi geometrica della scena che **integri, non duplichi**, le capacità già presenti nell'MCP upstream e l'autonomia di Codex nell'identificazione semantica degli oggetti.

### Sette capacità richieste

1. **Scene Inventory**: elencare figure, prop, camere, nodi e gerarchie con ID stabili, filtri e interrogazioni mirate per evitare dump voluminosi.
2. **Spatial Query**: leggere trasformazioni locali/world, orientamento, bounding box, dimensioni, distanze, relazioni e coordinate/unità dichiarate; distinguere stime da misure effettive.
3. **Surface Detection**: individuare superfici utilizzabili (letto, sedia, divano, pavimento ecc.) usando geometria, orientamento e dimensioni, senza affidarsi esclusivamente ai nomi dei nodi; restituire confidenza e alternative quando ambiguo.
4. **Contact Detection**: valutare distanza/contatto di piedi, mani, bacino e altre parti del corpo rispetto alle superfici, con tolleranze esplicite e indicazione di affidabilità.
5. **Collision Detection**: identificare possibili compenetrazioni fra figure e oggetti, indicando zona, coppia coinvolta e gravità; distinguere test approssimativi (bounding box) da test più precisi.
6. **Smart Placement**: proporre e, solo quando richiesto da Codex, applicare spostamenti/rotazioni per collocare personaggi su superfici, preservando per quanto possibile la posa e controllando contatti e collisioni.
7. **Scene Change Tracking**: confrontare snapshot/stato e restituire differenze compatte su oggetti e proprietà cambiate; gestire invalidazione cache e modifiche effettuate anche fuori dall'MCP.

### Workflow e vincoli

- Workflow tipico: identificazione personaggio/oggetto → rilevazione superficie → query spaziali → anteprima di placement → applicazione controllata → verifica contatti/collisioni → risultato strutturato sintetico a Codex.
- Analisi **read-only di default**; separare esplicitamente operazioni di lettura e mutazione.
- Prima delle mutazioni, prevedere snapshot/ripristino delle trasformazioni rilevanti e non alterare involontariamente pose, camere o altri elementi.
- Ottimizzare numero di chiamate e token: batch, filtri, output compatti, cache con invalidazione corretta. Non occultare incertezze, coordinate o limiti delle misure.
- Codex resta responsabile delle scelte di composizione e dei significati semantici; il modulo fornisce geometria e suggerimenti, non decide autonomamente l'intento creativo.
- Durante implementazione: verificare le API reali DAZ, riutilizzare MCP upstream, eseguire test incrementali in DAZ Studio e aggiornare procedure Markdown/Skills pertinenti.
- Questioni da chiarire: politica di applicazione delle correzioni automatiche, trattamento delle collisioni intenzionali e livello di accuratezza/prestazioni da privilegiare.

| 2026-10-28 | Confermata | Progettazione del modulo Scene Inspector & Spatial Intelligence con sette capacità, analisi read-only predefinita e placement verificabile. |

## Collisioni contestuali, materiali e personaggi non vestiti — decisioni confermate

- **Non tutte le intersezioni sono errori**: Contact/Collision Detection e Smart Placement devono distinguere tipo di superficie/oggetto, entità della penetrazione, intenzione della posa e fase del workflow.
- **Superfici morbide/deformabili** (materasso, letto, cuscini, divani): una penetrazione limitata del corpo può essere intenzionale/provvisoriamente accettabile perché la superficie potrà essere deformata in una fase successiva. Misurare e classificare, senza correggere indiscriminatamente; non presumere che ogni oggetto chiamato «bed» sia effettivamente deformabile.
- **Oggetti rigidi** (tazza, tavolo, pavimento): applicare criteri di collisione più severi, con tolleranze geometriche appropriate e distinzione tra collisioni gravi e piccoli errori di precisione.
- **Classificazione del materiale/rigidità**: Codex può fornire il contesto semantico; il modulo deve accettare proprietà/override espliciti e segnalare incertezza, evitando di inventare caratteristiche fisiche non disponibili nella scena.
- **Personaggi senza vestiti nella fase attuale**: considerare posa e contatti come **provvisori**. Vestiti, scarpe, capelli e deformazioni successive cambieranno ingombri, occlusioni e punti di contatto. Evitare ottimizzazioni premature e rivalidare dopo la vestizione.
- **Validazione per fasi**: (1) posa iniziale/anatomia/reference, (2) posizionamento e collisioni essenziali, (3) vestizione e nuove collisioni, (4) rifinitura finale di contatti, deformazioni e camere.
- **Esiti contestuali**: classificare problemi come accettabile provvisoriamente, da rivalutare dopo vestizione/deformazione, da correggere ora o incerto; includere misura, motivazione e confidenza.
- **Politica di correzione**: il modulo propone/calcola correzioni proporzionate al caso, mentre Codex decide se applicarle; non introdurre una regola universale di correzione automatica per tutte le collisioni. Conservare snapshot/ripristino e testare in DAZ Studio.

| 2026-10-28 | Confermata | Collisioni e contatti contestuali a rigidità/deformabilità, gravità e fase di lavorazione; posa senza vestiti provvisoria. |

## Deformazioni manuali e gestione dei props dell'environment — decisioni confermate

### Deformazioni delle superfici morbide
- Le deformazioni di materassi, cuscini, divani e altre superfici morbide sono **a carico dell'utente**, non devono essere applicate automaticamente da Codex o dal nuovo MCP.
- Durante posa, contatti e collisioni, il sistema deve identificare e registrare le **zone candidate a deformazione manuale**, con oggetto, personaggio/parte del corpo, punto o area e motivazione, distinguendo stime e casi incerti.
- **Alla fine del lavoro sulla scena**, Codex deve presentare all'utente un riepilogo operativo delle deformazioni da eseguire, anche se alcune sono solo suggerite e non obbligatorie. Non confondere questo promemoria con una richiesta di correzione automatica della posa.

### Libertà di modifica dei props e organizzazione della gerarchia
- Durante la composizione della scena Codex/AI è **libero di spostare, ruotare o nascondere i props dell'environment** quando serve all'inquadratura e alla disposizione dei personaggi, nel rispetto delle altre regole di sicurezza del progetto.
- **Ogni prop dell'environment di base che viene spostato/riutilizzato per la scena** deve essere rimosso dal gruppo gerarchico dell'environment di base e trasferito a un **gruppo dedicato ai props utilizzati/modificati nella scena**, così che sia immediatamente riconoscibile. Codex deve valutare se estendere lo stesso criterio ai props ruotati o altrimenti modificati; la regola esplicita riguarda almeno quelli spostati.
- Durante il reparenting preservare la trasformazione **world-space**, l'aspetto e i collegamenti rilevanti; evitare duplicazioni o alterazioni accidentali. La scelta del nome del gruppo e le eccezioni per gerarchie riggate/istanze vanno verificate in DAZ Studio.
- I props nascosti devono rimanere identificabili e gestibili, con stato di visibilità tracciabile, evitando cancellazioni non richieste.

### Aggiornamenti obbligatori in docs/
- **Durante l'implementazione**, aggiornare le procedure operative nel submodule Wiki `docs/`, in particolare `docs/Procedure-Scene-Posing-Completion.md`, includendo esplicitamente: libertà di spostare/nascondere props; trasferimento fuori dal gruppo dell'environment di base dei props riposizionati; conservazione delle trasformazioni world-space; raccolta delle deformazioni manuali; promemoria finale all'utente.
- Aggiornare anche eventuali altre procedure pertinenti e Skills nel repo `daz-mcp`, dopo test reali in DAZ Studio. Non modificare ora i documenti operativi: questa è la specifica per Codex.

| 2026-10-28 | Confermata | Deformazioni eseguite manualmente dall'utente, con promemoria finale delle aree da deformare. |
| 2026-10-28 | Confermata | Codex può spostare/nascondere props; quelli spostati escono dal gruppo environment di base e passano in un gruppo props utilizzati; aggiornare le procedure in docs/. |

## Gruppo Scene Props — decisione confermata

- Creare e utilizzare un gruppo DAZ denominato **`Scene Props`** per raccogliere **tutti i props utilizzati attivamente durante la composizione della scena** e **tutti i props originari dell'environment di base che vengono modificati, spostati, ruotati o altrimenti adattati**.
- Il gruppo va creato se assente e riutilizzato se già esistente, evitando duplicati. Non spostare indiscriminatamente l'intero environment statico che non è stato utilizzato o modificato.
- Quando un prop passa dall'environment di base a `Scene Props`, conservarne trasformazione world-space, visibilità, materiali e collegamenti necessari; verificare i casi particolari di gerarchie, istanze o vincoli prima di effettuare il reparenting.
- La libertà di Codex di nascondere props resta valida; se un prop è usato/modificato per la composizione, tracciarlo in `Scene Props` anche quando viene nascosto, senza cancellarlo.
- Aggiornare esplicitamente `docs/Procedure-Scene-Posing-Completion.md` e le altre procedure interessate durante l'implementazione, con verifica reale in DAZ Studio.

| 2026-10-28 | Confermata | Il gruppo dei props usati o modificati si chiama esattamente `Scene Props`; contiene anche i props spostati/modificati dall'environment di base. |

## Pose & Skeleton MCP — posa iniziale dalla libreria (decisione confermata)

- Per ciascun personaggio la **posa iniziale deve provenire da una posa esistente nella libreria DAZ**, non essere costruita direttamente da zero dalla stima dello scheletro AI.
- Codex cerca e seleziona una posa disponibile il più possibile simile alla reference, la mostra in anteprima quando previsto dalle procedure e la applica come base al Genesis 9.
- L'AI locale analizza la reference ricavando keypoint/scheletro, stima 3D e confidenze; il modulo Pose & Skeleton calcola le correzioni e adatta progressivamente la posa di libreria fino ad avvicinarla all'immagine di riferimento, rispettando limiti anatomici, rig e occlusioni.
- La posa iniziale è un punto di partenza, **non** un limite alla qualità o all'entità delle correzioni successive. Non confondere la scelta di una posa di libreria con la rinuncia alla stima AI o al retargeting.
- Verificare il risultato rispetto alla camera di riferimento, ai contatti e alle collisioni contestuali; ricordare che la posa senza vestiti è provvisoria.
- Codex deve verificare in DAZ Studio il funzionamento reale e aggiornare le procedure MD/Skills pertinenti durante l'implementazione.

| 2026-10-28 | Confermata | Pose & Skeleton parte sempre da una posa della libreria DAZ, poi la corregge sulla base dello scheletro stimato dalla reference. |

## Scene Validation MCP — classificazione finale (decisione confermata)

- Al termine della composizione, Codex deve eseguire una **validazione complessiva della scena**, producendo un rapporto sintetico e contestuale in tre categorie:
  1. **Problemi bloccanti**: errori sostanziali di posa, disposizione, camera, collisioni gravi o incoerenze che Codex deve tentare di risolvere prima di dichiarare completato il lavoro.
  2. **Problemi non bloccanti**: imperfezioni tollerabili nella fase corrente, da riportare senza impedire necessariamente la consegna.
  3. **Interventi manuali dell'utente**: deformazioni di materassi/cuscini/superfici morbide e altre rifiniture esplicitamente riservate all'utente.
- Codex valuta **gravità e categoria in base al contesto**, alle caratteristiche rigide/deformabili degli oggetti, all'intento creativo e alla fase del workflow (personaggi inizialmente senza vestiti); non usare soglie universali o correggere automaticamente ogni intersezione.
- Per ogni rilievo includere oggetto/i, posizione/zona se disponibile, motivazione, livello di confidenza e azione consigliata; distinguere problemi risolti, irrisolti e da verificare dopo vestizione.
- Il rapporto finale deve ricordare gli interventi manuali anche quando la scena è considerata pronta per la fase successiva.
- Durante implementazione Codex deve testare in DAZ Studio e aggiornare le procedure MD pertinenti in `docs/` e la documentazione del nuovo MCP.

| 2026-10-28 | Confermata | Scene Validation distingue problemi bloccanti, non bloccanti e interventi manuali; Codex valuta la gravità contestualmente. |

## Batch Operations MCP — rollback intelligente (decisione confermata)

- Le operazioni in batch devono supportare **dipendenze esplicite** tra modifiche e raggruppamenti coerenti.
- Se una modifica fallisce, **ripristinare il gruppo di operazioni dipendenti** per evitare stati parziali o incoerenti; **conservare le operazioni indipendenti riuscite**.
- Prima di mutazioni rilevanti, acquisire lo stato necessario al ripristino (trasformazioni, posa, camere, gerarchie, visibilità e altre proprietà effettivamente modificate). Non presumere atomicità transazionale nativa di DAZ Studio: Codex deve progettare e testare compensazioni e limiti.
- Restituire un report strutturato e compatto con operazioni riuscite, fallite, saltate, ripristinate e quelle per cui il rollback non è stato possibile; non dichiarare un rollback riuscito senza verificarlo.
- Applicare la stessa logica a spostamenti di personaggi, modifiche articolari, camera, props e reparenting in `Scene Props`, rispettando l'indipendenza reale delle operazioni.
- Durante l'implementazione Codex deve eseguire test di errore a metà batch in DAZ Studio e aggiornare le procedure Markdown pertinenti.

| 2026-10-28 | Confermata | Batch Operations: rollback delle modifiche dipendenti e conservazione di quelle indipendenti riuscite. |
