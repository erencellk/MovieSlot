from .models import Register

def kullanici_context(request):
    kullanici = None
    if 'kullanici_id' in request.session:
        try:
            kullanici = Register.objects.get(id=request.session['kullanici_id'])
        except Register.DoesNotExist:
            pass

    return {'kullanici': kullanici}
