from django.shortcuts import render

# Create your views here.


article_data = [
    {
        'id': 'press-release-03-03-25-1',
        'title': 'The Sentry Announces Justyna Gudzowska as New Executive Director to Lead Fight Against Illicit Finance',
        'desc': '''this is all about the india
          <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus est laboriosam ea ipsum iure natus sunt rem odit eum eos porro fugit quam tenetur aliquam unde et, voluptas adipisci, quibusdam modi consectetur? Expedita, voluptates quam. Molestiae modi suscipit excepturi blanditiis id qui voluptatem commodi totam atque necessitatibus aliquid recusandae sint eaque maxime, voluptate nemo quibusdam itaque placeat facere corporis deserunt deleniti esse nobis fuga. Nam veniam provident itaque aut adipisci rerum repudiandae, eius pariatur atque aperiam mollitia delectus error optio doloribus. Possimus, eligendi. Exercitationem consectetur reprehenderit suscipit saepe? Quidem illum accusantium eveniet quam. Ex consequuntur nesciunt nulla provident minus quidem.</h3>  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas quas excepturi ea a neque expedita nihil minima, asperiores dolor quibusdam, quia est deserunt quis enim ad accusantium soluta? Repellat quas earum obcaecati, id, delectus excepturi in molestiae incidunt et deleniti quod est aliquam eaque placeat. Dolores autem dolor voluptates recusandae veritatis neque rerum? Similique nihil facilis numquam voluptate a omnis. Cumque et dolorum accusantium, accusamus hic vel illum libero praesentium reiciendis. Quas odio qui atque aut, commodi necessitatibus suscipit sapiente quia reiciendis eaque modi, vitae eligendi laudantium est at mollitia? Officia veniam modi alias ducimus natus. Tempora obcaecati, rem architecto commodi aliquid vero ipsam. Optio porro omnis eum nam quod maxime obcaecati quisquam harum rem nobis. Quia sapiente autem possimus, eveniet at eos sunt laudantium voluptatum et minus quas ad totam, blanditiis voluptates quo soluta ut. Ipsam suscipit in asperiores perspiciatis quod voluptate maiores, reprehenderit eligendi nesciunt quam placeat? Mollitia laboriosam inventore velit non officiis necessitatibus nulla. Doloribus, nulla ratione. Dolores a provident doloribus necessitatibus debitis adipisci eligendi quae fugiat, eos aliquid pariatur cupiditate animi atque cum dolorum dolor sequi dolore hic voluptatibus dignissimos qui. Consectetur, ipsam iure unde velit repellat qui neque? Soluta sed temporibus iste impedit consequuntur debitis!</h3>'''
    },
    {
        'id': 'press-release-03-03-25-1',
        'title': 'The Sentry Announces Justyna Gudzowska as New Executive Director to Lead Fight Against Illicit Finance',
        'desc': '''this is all about the america'
          <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus est laboriosam ea ipsum iure natus sunt rem odit eum eos porro fugit quam tenetur aliquam unde et, voluptas adipisci, quibusdam modi consectetur? Expedita, voluptates quam. Molestiae modi suscipit excepturi blanditiis id qui voluptatem commodi totam atque necessitatibus aliquid recusandae sint eaque maxime, voluptate nemo quibusdam itaque placeat facere corporis deserunt deleniti esse nobis fuga. Nam veniam provident itaque aut adipisci rerum repudiandae, eius pariatur atque aperiam mollitia delectus error optio doloribus. Possimus, eligendi. Exercitationem consectetur reprehenderit suscipit saepe? Quidem illum accusantium eveniet quam. Ex consequuntur nesciunt nulla provident minus quidem.</h3> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas quas excepturi ea a neque expedita nihil minima, asperiores dolor quibusdam, quia est deserunt quis enim ad accusantium soluta? Repellat quas earum obcaecati, id, delectus excepturi in molestiae incidunt et deleniti quod est aliquam eaque placeat. Dolores autem dolor voluptates recusandae veritatis neque rerum? Similique nihil facilis numquam voluptate a omnis. Cumque et dolorum accusantium, accusamus hic vel illum libero praesentium reiciendis. Quas odio qui atque aut, commodi necessitatibus suscipit sapiente quia reiciendis eaque modi, vitae eligendi laudantium est at mollitia? Officia veniam modi alias ducimus natus. Tempora obcaecati, rem architecto commodi aliquid vero ipsam. Optio porro omnis eum nam quod maxime obcaecati quisquam harum rem nobis. Quia sapiente autem possimus, eveniet at eos sunt laudantium voluptatum et minus quas ad totam, blanditiis voluptates quo soluta ut. Ipsam suscipit in asperiores perspiciatis quod voluptate maiores, reprehenderit eligendi nesciunt quam placeat? Mollitia laboriosam inventore velit non officiis necessitatibus nulla. Doloribus, nulla ratione. Dolores a provident doloribus necessitatibus debitis adipisci eligendi quae fugiat, eos aliquid pariatur cupiditate animi atque cum dolorum dolor sequi dolore hic voluptatibus dignissimos qui. Consectetur, ipsam iure unde velit repellat qui neque? Soluta sed temporibus iste impedit consequuntur debitis!</h3>'''
    },
    {
        'id': 'press-release-03-03-25-1',
        'title': 'The Sentry Announces Justyna Gudzowska as New Executive Director to Lead Fight Against Illicit Finance',
        'desc': '''this is all about the pakistan'
          <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus est laboriosam ea ipsum iure natus sunt rem odit eum eos porro fugit quam tenetur aliquam unde et, voluptas adipisci, quibusdam modi consectetur? Expedita, voluptates quam. Molestiae modi suscipit excepturi blanditiis id qui voluptatem commodi totam atque necessitatibus aliquid recusandae sint eaque maxime, voluptate nemo quibusdam itaque placeat facere corporis deserunt deleniti esse nobis fuga. Nam veniam provident itaque aut adipisci rerum repudiandae, eius pariatur atque aperiam mollitia delectus error optio doloribus. Possimus, eligendi. Exercitationem consectetur reprehenderit suscipit saepe? Quidem illum accusantium eveniet quam. Ex consequuntur nesciunt nulla provident minus quidem.</h3> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas quas excepturi ea a neque expedita nihil minima, asperiores dolor quibusdam, quia est deserunt quis enim ad accusantium soluta? Repellat quas earum obcaecati, id, delectus excepturi in molestiae incidunt et deleniti quod est aliquam eaque placeat. Dolores autem dolor voluptates recusandae veritatis neque rerum? Similique nihil facilis numquam voluptate a omnis. Cumque et dolorum accusantium, accusamus hic vel illum libero praesentium reiciendis. Quas odio qui atque aut, commodi necessitatibus suscipit sapiente quia reiciendis eaque modi, vitae eligendi laudantium est at mollitia? Officia veniam modi alias ducimus natus. Tempora obcaecati, rem architecto commodi aliquid vero ipsam. Optio porro omnis eum nam quod maxime obcaecati quisquam harum rem nobis. Quia sapiente autem possimus, eveniet at eos sunt laudantium voluptatum et minus quas ad totam, blanditiis voluptates quo soluta ut. Ipsam suscipit in asperiores perspiciatis quod voluptate maiores, reprehenderit eligendi nesciunt quam placeat? Mollitia laboriosam inventore velit non officiis necessitatibus nulla. Doloribus, nulla ratione. Dolores a provident doloribus necessitatibus debitis adipisci eligendi quae fugiat, eos aliquid pariatur cupiditate animi atque cum dolorum dolor sequi dolore hic voluptatibus dignissimos qui. Consectetur, ipsam iure unde velit repellat qui neque? Soluta sed temporibus iste impedit consequuntur debitis!</h3>'''
    },
    {
        'id': 'press-release-03-03-25-1',
        'title': 'The Sentry Announces Justyna Gudzowska as New Executive Director to Lead Fight Against Illicit Finance',
        'desc': '''this is all about the bangladesh'
          <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus est laboriosam ea ipsum iure natus sunt rem odit eum eos porro fugit quam tenetur aliquam unde et, voluptas adipisci, quibusdam modi consectetur? Expedita, voluptates quam. Molestiae modi suscipit excepturi blanditiis id qui voluptatem commodi totam atque necessitatibus aliquid recusandae sint eaque maxime, voluptate nemo quibusdam itaque placeat facere corporis deserunt deleniti esse nobis fuga. Nam veniam provident itaque aut adipisci rerum repudiandae, eius pariatur atque aperiam mollitia delectus error optio doloribus. Possimus, eligendi. Exercitationem consectetur reprehenderit suscipit saepe? Quidem illum accusantium eveniet quam. Ex consequuntur nesciunt nulla provident minus quidem.</h3> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas quas excepturi ea a neque expedita nihil minima, asperiores dolor quibusdam, quia est deserunt quis enim ad accusantium soluta? Repellat quas earum obcaecati, id, delectus excepturi in molestiae incidunt et deleniti quod est aliquam eaque placeat. Dolores autem dolor voluptates recusandae veritatis neque rerum? Similique nihil facilis numquam voluptate a omnis. Cumque et dolorum accusantium, accusamus hic vel illum libero praesentium reiciendis. Quas odio qui atque aut, commodi necessitatibus suscipit sapiente quia reiciendis eaque modi, vitae eligendi laudantium est at mollitia? Officia veniam modi alias ducimus natus. Tempora obcaecati, rem architecto commodi aliquid vero ipsam. Optio porro omnis eum nam quod maxime obcaecati quisquam harum rem nobis. Quia sapiente autem possimus, eveniet at eos sunt laudantium voluptatum et minus quas ad totam, blanditiis voluptates quo soluta ut. Ipsam suscipit in asperiores perspiciatis quod voluptate maiores, reprehenderit eligendi nesciunt quam placeat? Mollitia laboriosam inventore velit non officiis necessitatibus nulla. Doloribus, nulla ratione. Dolores a provident doloribus necessitatibus debitis adipisci eligendi quae fugiat, eos aliquid pariatur cupiditate animi atque cum dolorum dolor sequi dolore hic voluptatibus dignissimos qui. Consectetur, ipsam iure unde velit repellat qui neque? Soluta sed temporibus iste impedit consequuntur debitis!</h3>'''
    },
    {
        'id': 'press-release-03-03-25-1',
        'title': 'The Sentry Announces Justyna Gudzowska as New Executive Director to Lead Fight Against Illicit Finance',
        'desc': '''this is all about the china'
          <h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus est laboriosam ea ipsum iure natus sunt rem odit eum eos porro fugit quam tenetur aliquam unde et, voluptas adipisci, quibusdam modi consectetur? Expedita, voluptates quam. Molestiae modi suscipit excepturi blanditiis id qui voluptatem commodi totam atque necessitatibus aliquid recusandae sint eaque maxime, voluptate nemo quibusdam itaque placeat facere corporis deserunt deleniti esse nobis fuga. Nam veniam provident itaque aut adipisci rerum repudiandae, eius pariatur atque aperiam mollitia delectus error optio doloribus. Possimus, eligendi. Exercitationem consectetur reprehenderit suscipit saepe? Quidem illum accusantium eveniet quam. Ex consequuntur nesciunt nulla provident minus quidem.</h3> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas quas excepturi ea a neque expedita nihil minima, asperiores dolor quibusdam, quia est deserunt quis enim ad accusantium soluta? Repellat quas earum obcaecati, id, delectus excepturi in molestiae incidunt et deleniti quod est aliquam eaque placeat. Dolores autem dolor voluptates recusandae veritatis neque rerum? Similique nihil facilis numquam voluptate a omnis. Cumque et dolorum accusantium, accusamus hic vel illum libero praesentium reiciendis. Quas odio qui atque aut, commodi necessitatibus suscipit sapiente quia reiciendis eaque modi, vitae eligendi laudantium est at mollitia? Officia veniam modi alias ducimus natus. Tempora obcaecati, rem architecto commodi aliquid vero ipsam. Optio porro omnis eum nam quod maxime obcaecati quisquam harum rem nobis. Quia sapiente autem possimus, eveniet at eos sunt laudantium voluptatum et minus quas ad totam, blanditiis voluptates quo soluta ut. Ipsam suscipit in asperiores perspiciatis quod voluptate maiores, reprehenderit eligendi nesciunt quam placeat? Mollitia laboriosam inventore velit non officiis necessitatibus nulla. Doloribus, nulla ratione. Dolores a provident doloribus necessitatibus debitis adipisci eligendi quae fugiat, eos aliquid pariatur cupiditate animi atque cum dolorum dolor sequi dolore hic voluptatibus dignissimos qui. Consectetur, ipsam iure unde velit repellat qui neque? Soluta sed temporibus iste impedit consequuntur debitis!</h3>'''
    }
]



def base_home(request):
    return render (request, 'base_home.html', {'article_data': article_data})

def about(request):
    return render(request,'about.html')

def eduaction(request):
    return render(request, 'eduaction.html', {'article_data': article_data})

def social_media(request):
    return render(request , 'social_media.html' , {'article_data': article_data})

def business(request):
    return render(request, 'Business.html', {'article_data': article_data})

def politics(request):
    return render(request, 'politics.html', {'article_data': article_data})

def goverment(request):
    return render(request , 'goverment.html' , {'article_data': article_data})

def economy(request):
    return render(request ,'economy.html',{'article_data':article_data})

def health(request):
    return render(request ,'health.html',{'article_data':article_data})

def crime(request):
    return render(request , 'crime.html',{'article_data':article_data})


def read(request,pk):
    for i in article_data:
        if i['id'] == pk:
            return render (request, 'read.html' , {'data' : i})
        
def read_eduaction(request,pk):
    for i in article_data:
        if i['id'] == pk:
            return render(request, 'read_eduaction.html', {'data':i})


def read_social_media(request, pk):
    for i in article_data:
        if i['id'] == pk:
            return render(request, 'read_social_media.html', {'data': i})

def read_business(request, pk):
    for i in article_data:
        if i['id'] == pk:
            return render(request, 'read_business.html', {'data': i})


def read_politics(request, pk):
    for i in article_data:
        if i ['id'] == pk:
            return render(request , 'read_politics.html' , {'data' : i})
        

def read_goverment(request, pk):
    for i in article_data:
        if i ['id'] == pk:
            return render(request , 'read_goverment.html' , {'data' : i})
        

def read_economy(request, pk):
    for i in article_data:
        if i ['id'] == pk:
            return render(request , 'read_economy.html' , {'data' : i})
        
def read_health(request, pk):
    for i in article_data:
        if i ['id'] == pk:
            return render(request , 'read_health.html' , {'data' : i})
        

def read_crime(request, pk):
    for i in article_data:
        if i ['id'] == pk:
            return render(request , 'read_crime.html' , {'data' : i})

