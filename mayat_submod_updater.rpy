# Legacy Submod Updater Plugin support

init -989 python:
    legacy_submod_api = getattr(store.mas_submod_utils, "Submod", None)
    sup_utils = getattr(store, "sup_utils", None)

    if (
        legacy_submod_api is not None
        and store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin")
        and sup_utils is not None
        and hasattr(sup_utils, "SubmodUpdater")
    ):
        sup_utils.SubmodUpdater(
            submod="MayAT",
            user_name="Kapiqiano7",
            repository_name="MayAT",
            tag_formatter=lambda tag: tag.lstrip("v")
        )
