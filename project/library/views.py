from utils import JsonResponse

def like(request, obj_id, model):
    """
    Upticks an item's ``liked`` count. Returns JSON.
    """
    try:
        obj = model.objects.get(pk=obj_id)
    except model.DoesNotExist:
        return JsonResponse({'stat': 'fail', 'msg': 'Error: item not found'})
    sess_key = 'has_voted_on_%s_%s' % (model._meta.object_name, obj_id)
    if request.session.get(sess_key):
        return JsonResponse({'stat': 'fail', 'msg': 'Error: you\'ve already voted'})
    obj.liked += 1
    obj.save()
    request.session[sess_key] = True
    return JsonResponse({'stat': 'ok', 'msg': 'Thanks for your vote!', 'likes': obj.liked})