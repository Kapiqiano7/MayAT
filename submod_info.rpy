# Legacy Submod registration

init -990 python:
    legacy_submod_api = getattr(store.mas_submod_utils, "Submod", None)

    if legacy_submod_api is not None:
        legacy_submod_api(
            author="Kapiqiano",
            name="MayAT",
            description="Technology and computing conversations with Monika. The first collection covers Ubuntu, Arch Linux, Fedora, Linux Mint, and Debian.",
            version="1.0.3"
        )
