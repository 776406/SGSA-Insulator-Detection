# Third-party notices and source provenance

This component pre-release is distributed under GNU AGPL-3.0-only. The complete GNU Affero General Public License version 3 text is provided in `LICENSE` without modification. Supplied Ultralytics source-license notices are retained. SPDX identifiers and package metadata use the same AGPL-3.0-only expression; no MIT alternative is offered for this combined release.

Upstream project lineage:

- Ultralytics: https://github.com/ultralytics/ultralytics
- YOLOv13: https://github.com/iMoonLab/yolov13

Inherited components include standard CIoU geometry, Distribution Focal Loss, distance-target conversion and baseline feature-block designs. Their inclusion is not a claim that these algorithms originated in SGSA. The optional adapters import baseline blocks from a separately installed compatible framework; they do not bundle the full framework.

The available local snapshot does not establish the exact upstream revision. The links above identify provenance and do not certify a match to current upstream code.

Local changes on 2026-11-21: standalone distance conversion consolidated into the geometry module; package exports and examples updated to the component scope; license identifiers and distribution metadata aligned. This pre-release includes updated release-status documentation and version metadata, with architecture references, automated tests, validation records and file manifests reserved for a subsequent component release. Retained SGCA, CIoU, QGI-CIoU and DFL computation is unchanged.

The license text's Free Software Foundation copyright applies to the license document. Existing source attribution and third-party rights remain applicable. This release adds no research-only, noncommercial, confidentiality or anti-reuse restriction to upstream AGPL-covered code.
