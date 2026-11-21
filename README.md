# SGSA core components

> **Pre-release: files are being uploaded in stages.** This initial release provides the core SGCA and QGI-CIoU implementations. Model configuration files, automated component tests, validation records, file manifests and additional documentation are planned for a subsequent component release. The repository will be updated as these materials are prepared.

## Currently available

- **SGCA**: Semantic-Guided Collaborative Attention.
- **QGI-CIoU**: Quality-Gated Inner-CIoU for bounding-box regression, with the DFL branch and supporting box geometry.
- Optional feature-block adapters for compatible YOLOv9, YOLO11 and YOLOv13 implementations.
- A small synthetic example for checking component execution and gradients.
- Installation metadata, the license and third-party notices.

## Release scope

This repository is currently a **core-component pre-release**. Model configuration files and the automated test suite are not included in this snapshot. Training and evaluation entry points, datasets, data splits, trained checkpoints and experiment logs are also outside the current release.

The available files alone are insufficient to reproduce the reported detector results. The planned component update should not be interpreted as a commitment to provide a complete end-to-end experiment reproduction package.

## Repository contents

```text
sgsa/
  modules/sgca.py           SGCA feature module
  losses/loss.py           QGI-CIoU regression and DFL
  losses/metrics.py        Box geometry and distance-target conversion
  adapters/ultralytics.py  Optional baseline block wrappers
examples/
  check_components.py     Synthetic execution example
pyproject.toml            Package metadata and build settings
requirements.txt          Core runtime dependency
MANIFEST.in               Source-distribution file selection
LICENSE                   GNU AGPL version 3 license text
THIRD_PARTY_NOTICES.md     Upstream provenance and modification notices
.gitignore                Local files excluded from Git tracking
```

Python package directories also contain `__init__.py` files for imports and package organization.

## Quick check

The standalone core requires **Python 3.10+** and **PyTorch 2.2+**. With PyTorch available, run from the repository root:

```bash
python -m examples.check_components
```

An editable installation is optional:

```bash
python -m pip install -e .
```

The example prints feature shapes, a standalone SGCA parameter count, a regression loss and finite-gradient checks using synthetic inputs. It does not train a detector or measure detection accuracy or speed. The standalone core does not require Ultralytics or FlashAttention.

## Component notes

SGCA uses depthwise 5x5 and pointwise 1x1 convolutions, BatchNorm and SiLU, followed by spatial attention, channel attention and residual addition.

The QGI-CIoU regression defaults are auxiliary ratio **0.75**, mode **both**, quality threshold **0.50**, gate exponent **2.0** and maximum auxiliary weight **0.30**. These settings are read from environment variables when `BboxLoss` is constructed.

`BboxLoss` returns separate box-regression and DFL losses. Its caller supplies positive-box masks, target-score weights and a positive normalization denominator, uses consistent coordinate units and skips the call when no positive boxes are present. Detector-wide loss gains are applied by the caller.

The optional adapters need a compatible external framework exposing `RepNCSPELAN4`, `C3k2`, `A2C2f` and `DSC3k2` in `ultralytics.nn.modules.block`, with matching constructor signatures. They also require appropriate registration in the external model parser. A generic Ultralytics installation is not a compatibility guarantee. Importing these components does not automatically modify another framework's model or training loss.

## Planned component update

- Architecture configuration references for the supported baseline families.
- Automated component tests and validation scope documentation.
- Validation records and a file-integrity manifest for the corresponding release.
- Additional implementation and compatibility notes.

## License and provenance

This release is licensed under **GNU AGPL-3.0-only**. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

The code builds on Ultralytics and YOLOv13-based implementations. Standard CIoU geometry, Distribution Focal Loss and baseline block designs are inherited components. Upstream notices are retained; the exact historical upstream revision has not been established.
