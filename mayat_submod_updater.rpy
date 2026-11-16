# Legacy Submod Updater Plugin support

init -989 python:
    _mayat_submod_api = getattr(
        store.mas_submod_utils, "Submod", None
    )
    _mayat_is_installed = getattr(
        store.mas_submod_utils, "isSubmodInstalled", None
    )
    _mayat_sup_utils = getattr(store, "sup_utils", None)
    _mayat_submod_map = getattr(
        store.mas_submod_utils, "submod_map", {}
    )

    if (
        _mayat_submod_api is not None
        and callable(_mayat_is_installed)
        and _mayat_is_installed("Submod Updater Plugin")
        and "MayAT" in _mayat_submod_map
        and _mayat_sup_utils is not None
        and callable(getattr(_mayat_sup_utils, "SubmodUpdater", None))
    ):
        _mayat_sup_utils.SubmodUpdater(
            submod="MayAT",
            user_name="Kapiqiano7",
            repository_name="MayAT",
            tag_formatter=lambda tag: tag.lstrip("v")
        )
