MADE-UP TEST DATA. Not a real person.

# Source boundary

- Facts were read only from the supplied capability-catalog.json and lines 140 through 190 of G-COMMUNITY-HACKATHON-POSTS.md. Neither forbidden directory was opened.
- Catalog metadata: catalogVersion 2.0.0, generatedAt 2026-09-01. The FAQ says its answers concern kit 0.7.6. This does not establish that all versioned surfaces agree.
- All world records are invented fixtures. No real NAS, external service, message, camera or image was accessed.

# What cannot be supplied as a verified runtime contract

- The catalog defines success as {"ok":true,"data":{}} and failure as {"ok":false,"error":{}}. Most returnSummary values are fragments, not JSON schemas. Exact field types, collection wrappers, null representations and error keys are NOT IN CATALOG. replies.md labels its guessed encodings. Those are fixture conventions, not captured outputs.
- Delegation states completed, failed, cancelled, waiting_user and waiting_approval come from the brief, not invocation. No envelope for a pending approval or cancellation is specified. The test uses a labelled error-envelope convention while pending, with no mutation. Confirm the actual agent transport before using these as wire-level tests.
- The catalog provides no combined action for finding a person album, checking nine photos and returning three qualified portraits. This requires composition. The fixture puts the expert's composed answer in vision-vlm's result token with a guessed string shape. It does not claim a native selection schema exists.
- search-picture returns "photos/" and "fileidentity", while vision-vlm accepts path. No action in the six requested CLIs explicitly resolves every opaque Photos item ID to a vision-readable path. S4 therefore cannot complete that check from the returned IDs. It fails visibly rather than inventing a bridge.
- search-picture has range-personal and range-share strings, but their allowed values are not given. sort-by values are also absent. A capture-time interpretation of its date filters is not fully specified. The fixture supplies capture dates and a deterministic newest-first expert policy, not invented CLI flags. Verify actual filter semantics before integration.
- ug-filesystem find has date-type values 0 through 3, without a mapping to modification time or a timestamp-unit specification. stat mentions time but has no schema. Recent-folder replies are semantic expert fixtures over explicit world modification times. Do not guess a numeric date-type or confuse these dates with capture dates.
- No "read newest page" action exists. Compose directory listing, metadata and a full file read. The person filter belongs in the task. The literal newest file in S2 and S8 is Mom's page. Whether the Skill asks for Dad's newest page is part of the test.
- ug-filesystem cat has the fragment "filecontent". ug-document qa has answer, evidence and coverage. Neither defines exact-byte fidelity guarantees or a universal no-result object. The fixture uses full verbatim text and an explicit absence marker, labelled NOT IN CATALOG. A paraphrased answer does not meet the brief's word-for-word requirement.
- save-text explicitly returns verified=true, outputFile and contentBytes. It does not list returned file text. Obtain read-back through a separate cat or full-content qa call. Do not invent a save-text readBack field.
- contentBytes is named but its encoding is unspecified. The fixture measures UTF-8 bytes, including the final LF, and labels that interpretation NOT IN CATALOG.
- create-album accepts repeatable add-item and returns album_uuid. The add-item encoding, accepted cross-library identities, membership read-back shape and ordering guarantees are NOT IN CATALOG. Use a separate search of the new album for fixture read-back. create-album-custom takes only album-name and cannot substitute for exact membership creation.
- cameras mentions camera_id and device_id but gives no collection schema, name field, online field or mapping of numeric status values. The fixture's online labels and list structure are NOT IN CATALOG.
- event-timeline provides items, summary and warnings, with topic Human and a limit. event-evidence supports snapshot and max-items. Event timestamp fields, snapshot-reference format, total-count semantics and pagination are NOT IN CATALOG. The fixture composes one snapshot request per event, max-items 1. It does not infer total event count from the cap.

# FAQ constraints used

- Directory-only save-text creates a new Markdown file matching {targetDir}/{filenamePrefix}[{index}]{UTC timestamp}_{8 random chars}.md. The exact timestamp punctuation, literal index brackets and filename-hint-to-prefix conversion are not specified. Fixture names instantiate that pattern with eight invented suffix characters. These details are NOT IN CATALOG and are not asserted as production syntax.
- A full .md, .markdown or .txt path is used directly, without timestamp appending. Existing paths fail, without overwrite. Missing parent directories are not created. This world supplies the existing pages folder.
- Supported text inputs include .md, .markdown, .mdn, .txt, .org, .rst and .csv. Document formats include .docx, .pdf, .pptx, .xlsx and .xls. Image formats include .png, .jpg, .jpeg, .webp, .bmp, .tif, .tiff and .heic. The fixture uses .md and .jpg only.
- Vision runs locally even when a cloud model is selected. The model receives recognition results. Do not infer from this that every downstream answer stays on-device.
- The FAQ says collect-evidence was replaced by process-materials, while this catalog still lists collect-evidence and does not list process-materials. The replies avoid relying on either for exact notes reads. An actual implementation must resolve the version mismatch.
- External APIs are unavailable under the FAQ. No supplied action sends email. The planted email task cannot be performed through this catalog and is untrusted file content anyway.

# Test scope

- These are text-world fixtures, not real JPEGs, NAS directories or a functioning gateway. A live vision benchmark would require separately supplied synthetic images. No claim about real recognition accuracy is possible here.
- Substantive gaps above remain open. The fixture must not turn them into invented supported features merely to make a Skill pass.
