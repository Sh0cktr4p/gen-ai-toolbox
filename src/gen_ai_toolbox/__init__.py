from omegaconf import OmegaConf

from . import training


def run_with_config(config: OmegaConf):
    generative_model = training.generative_model_from_config(config)

    if hasattr(config, "training") and config.training is not None and not \
            (hasattr(config, "eval_only") and config.eval_only):
        training.train_from_config(config, generative_model)
    else:
        generative_model.render_batch(
            n_rows=4,
            n_columns=4,
        )
