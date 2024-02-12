from site_setup import models

# Este local será usado para guardar contextos globais


def site_setup(request):
    setup = models.SiteSetup.objects.order_by('-id').first()


    return {
        'setup': setup
    }