from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, LinkForm, ExperienceForm, EducationForm, SkillForm
from .models import User, Link, Experience, Education, Skill

# Create your views here.
def cadastrar_curriculo(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        link_form = LinkForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        education_form = EducationForm(request.POST)
        skill_form = SkillForm(request.POST)

        if user_form.is_valid() and link_form.is_valid() and experience_form.is_valid() and education_form.is_valid() and skill_form.is_valid():
            user = user_form.save()
            link = link_form.save(commit=False)
            link.user = user
            link.save()
            experience = experience_form.save(commit=False)
            experience.user = user
            experience.save()
            education = education_form.save(commit=False)
            education.user = user
            education.save()
            skill = skill_form.save(commit=False)
            skill.user = user
            skill.save()
            return redirect('sucesso')
    else:
        user_form = UserForm()
        link_form = LinkForm()
        experience_form = ExperienceForm()
        education_form = EducationForm()
        skill_form = SkillForm()
    return render(request, 'cadastro_curriculo.html', {'user_form': user_form, 'link_form': link_form, 'experience_form': experience_form, 'education_form': education_form, 'skill_form': skill_form})

def sucesso(request):
    return render(request, 'sucesso.html')

def listar_curriculos(request):
    curriculos = User.objects.all()
    return render(request, 'listar_curriculos.html', {'curriculos': curriculos})

def editar_curriculos(request, user_id):
    curriculo = get_object_or_404(User, pk=user_id)
    links = Link.objects.filter(user=curriculo)
    experiences = Experience.objects.filter(user=curriculo)
    educations = Education.objects.filter(user=curriculo)
    skills = Skill.objects.filter(user=curriculo)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=curriculo)
        link_form = LinkForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        education_form = EducationForm(request.POST)
        skill_form = SkillForm(request.POST)

        if user_form.is_valid() and link_form.is_valid() and experience_form.is_valid() and education_form.is_valid() and skill_form.is_valid():
            user_form.save()
            link = link_form.save(commit=False)
            link.user = curriculo
            link.save()
            experience = experience_form.save(commit=False)
            experience.user = curriculo
            experience.save()
            education = education_form.save(commit=False)
            education.user = curriculo
            education.save()
            skill = skill_form.save(commit=False)
            skill.user = curriculo
            skill.save()
            return redirect('sucesso')
    else:
        user_form = UserForm(instance=curriculo)
        link_form = LinkForm()
        experience_form = ExperienceForm()
        education_form = EducationForm()
        skill_form = SkillForm()

    return render(request, 'visualizar_curriculo.html', {
        'curriculo': curriculo, 
        'user_form': user_form, 
        'links': links, 
        'experiences': experiences, 
        'educations': educations, 
        'skills': skills,
        'link_form': link_form,
        'experience_form': experience_form,
        'education_form': education_form,
        'skill_form': skill_form,
    })