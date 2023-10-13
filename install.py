import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("Flask"):
    launch.run_pip("install Flask", "requirements for Translate api")
