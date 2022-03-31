
from torchvision.transforms import transforms

import online.config as cfg

class DefaultTransforms:
    normalize = transforms.Normalize(mean=cfg.IMAGENET_MEAN,
                                     std=cfg.IMAGENET_STD)

    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        normalize,
    ])

    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        normalize,
    ])
