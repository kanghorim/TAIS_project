from django.shortcuts import redirect, render
from comm.models import Board
from member.models import User_Info  
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Max

# Create your views here.
def community(request):
    nowpage = int(request.GET.get('nowpage', 1))
    if request.method == 'GET' :
        qs = Board.objects.all().order_by('-b_group','-b_step')
        paginator = Paginator(qs,5)
        community = paginator.get_page(nowpage)
        context = {'community' : community, 'nowpage' : nowpage}
        return render(request,'comm/community.html',context)

    else :
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        if category == 'title' :
            qs = Board.objects.filter(b_title__contains = searchword)
            paginator = Paginator(qs,5)
            community = paginator.get_page(nowpage)
            context = {'community' : community, 'nowpage' : nowpage, 'category' : category, 'searchword' : searchword}
            return render(request,'comm/community.html',context)
        elif category == 'content' :
            qs = Board.objects.filter(b_content__contains = searchword)
            paginator = Paginator(qs,5)
            community = paginator.get_page(nowpage)
            context = {'community' : community, 'nowpage' : nowpage, 'category' : category, 'searchword' : searchword}
            return render(request,'comm/community.html',context)
        elif category == 'all' :
            qs = Board.objects.filter(Q(b_title__contains = searchword) | Q(b_content__contains = searchword))
            paginator = Paginator(qs,5)
            community = paginator.get_page(nowpage)
            context = {'community' : community, 'nowpage' : nowpage,'category' : category, 'searchword' : searchword}
            return render(request,'comm/community.html',context)

def community_view(request, board_no):
    qs = Board.objects.get(board_no = board_no)
    qs.b_count += 1
    qs.save()
    context = {'community' : qs }
    
    return render(request, 'comm/community_view.html', context)

def community_write(request):
    return render(request, 'comm/community_write.html')
        
def community_writeOk(request) :
    id = request.POST.get('id')
    member = User_Info.objects.get(user_id = id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # img = request.FILES.get('img', '')
    no = User_Info.objects.aggregate(max_b_hit = Max('b_count'))
    max_no = no['max_b_no']
    max_no += 1
    b_no = max_no
    
    qs = Board(board_no = b_no, user_id=member, b_title=title, b_content=content)
    qs.save()

    return redirect('comm/community.html')