def filterpost(request , url, klass=False, items = 10):
    '''The 'filter post' function does a content filtering with the 'klass' parameter, and limits the 
        number of items that will appear on the page with the 'items' parameter, and also receives it.
        The 'url' parameter receives the same URL that will be returned with the render function. The 'request' 
        parameter receives the page request.'''
    
    date = datetime.datetime.now().year
    
    if klass == False:
        list_posts = Content.objects.all() #Content 'in this case is the class that represents the posts on Models

    else:
        list_posts = Content.objects.filter(categoria = klass)
    
    paginator = Paginator(list_posts, items)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request , url, {'posts':posts})
