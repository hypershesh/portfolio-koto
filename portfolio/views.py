from django.contrib import messages
from django.shortcuts import redirect, render


PROJECTS = [
    {
        "number": "01",
        "title": "Service Desk",
        "type": "IT support / Process improvement",
        "description": "A streamlined ticket workflow that helps teams resolve incidents faster, document fixes, and keep users informed.",
        "tags": ["Microsoft 365", "Documentation"],
        "accent": "coral",
    },
    {
        "number": "02",
        "title": "SecureNet",
        "type": "Network administration / Security",
        "description": "A small-business network refresh with improved access controls, device management, backups, and monitoring.",
        "tags": ["Networking", "Cybersecurity"],
        "accent": "mint",
    },
    {
        "number": "03",
        "title": "CloudOps",
        "type": "Cloud infrastructure / Automation",
        "description": "A repeatable deployment setup for a growing team, reducing manual configuration and making environments easier to maintain.",
        "tags": ["AWS", "Python scripting"],
        "accent": "sun",
    },
]


def home(request):
    return render(request, "portfolio/home.html", {"projects": PROJECTS})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        if name and email and message:
            messages.success(request, "Thanks for reaching out. I will be in touch soon.")
        else:
            messages.error(request, "Please complete all fields before sending.")
    return redirect("portfolio:home")
