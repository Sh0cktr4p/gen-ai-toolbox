from omegaconf import OmegaConf
import hydra

from gen_ai_toolbox import run_with_config


@hydra.main(
    config_path="config",
    config_name="celebrity-diffusion",
    version_base=None
)
def main(cfg: OmegaConf):
    run_with_config(cfg)


if __name__ == "__main__":
    main()
