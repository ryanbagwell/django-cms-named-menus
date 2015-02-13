try:
    from django.apps import AppConfig

    class CMSNamedMenusConfig(AppConfig):
        name = 'cms_named_menus'
        verbose_name = "CMS Menus"

    default_app_config = 'cms_named_menus.CMSNamedMenusConfig'
except:
    pass
