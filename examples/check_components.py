# Local release update: 2026-11-21.
"""Run with: python -m examples.check_components (from the repository root)."""

import torch

from sgsa import BboxLoss, SGCA


def main():
    torch.manual_seed(0)
    torch.set_num_threads(1)
    module = SGCA(64)
    features = torch.randn(2, 64, 20, 20, requires_grad=True)
    output = module(features)
    output.square().mean().backward()
    print(f"SGCA: {tuple(features.shape)} -> {tuple(output.shape)}")
    print(f"SGCA parameters at C=64: {sum(p.numel() for p in module.parameters())}")
    print(f"SGCA input gradient finite: {torch.isfinite(features.grad).all().item()}")

    # Synthetic positive boxes and weights for a standalone regression check.
    pred = torch.tensor([[[.2, .2, 10.2, 10.2], [.5, .5, 10.5, 10.5]]], requires_grad=True)
    target = torch.tensor([[[0., 0., 10., 10.], [0., 0., 10., 10.]]])
    anchors = torch.tensor([[5., 5.], [5., 5.]])
    scores = torch.tensor([[[.9, 0.], [.8, 0.]]])
    fg = torch.tensor([[True, True]])
    criterion = BboxLoss(reg_max=1)  # Disable only DFL for this box-regression example.
    loss, dfl = criterion(torch.zeros(1, 2, 4), pred, anchors, target, scores, scores.sum(), fg)
    loss.backward()
    print(f"QGI-CIoU regression loss: {loss.item():.6f}; DFL: {dfl.item():.1f}")
    print(f"Regression gradient finite: {torch.isfinite(pred.grad).all().item()}")
    print(f"Regression settings: ratio={criterion.inner_iou_fixed_ratio}, mode={criterion.inner_iou_mode}, tau={criterion.qg_tau}, gamma={criterion.qg_gamma}, lambda_max={criterion.qg_lambda_max}")


if __name__ == '__main__':
    main()
