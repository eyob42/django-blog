# 📝 Django Personal Blog

A beautiful and fully-featured **personal blog** built with **Django** and **Tailwind CSS**, deployed on **Render**.

---

## 🌐 Live Demo

- **Live Site:** [https://django-blog-pmcn.onrender.com](https://django-blog-pmcn.onrender.com)
- **Admin Panel:** [https://django-blog-pmcn.onrender.com/admin](https://django-blog-pmcn.onrender.com/admin)

---

## ✨ Features

- 🖋️ **Modern Design** – Clean, responsive layout with Tailwind CSS
- 📰 **Blog Posts** – Create, read, update, and delete posts
- 🗂️ **Categories** – Organize posts with categories
- 💬 **Comments** – User comment system with forms
- ⚙️ **Admin Panel** – Full Django admin interface for content management
- 📱 **Responsive** – Works perfectly on all devices

---

# Django Personal Blog

A beautiful, fully-featured personal blog built with Django and Tailwind CSS, deployed on Render.

## 🌐 Live Demo

**Live Site:** https://django-blog-pmcn.onrender.com  
**Admin Panel:** https://django-blog-pmcn.onrender.com/admin

## ✨ Features

- **Modern Design** - Clean, responsive layout with Tailwind CSS
- **Blog Posts** - Create, read, update, and delete blog posts
- **Categories** - Organize posts with categories
- **Comments** - User comment system with forms
- **Admin Panel** - Full Django admin interface for content management
- **Responsive** - Works perfectly on all devices

## 🛠️ Tech Stack

- **Backend:** Django 5.2.7
- **Frontend:** Tailwind CSS, HTML5
- **Database:** SQLite
- **Deployment:** Render.com
- **WSGI Server:** Gunicorn

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/eyob42/django-blog.git
   cd django-blog
   ```

2. **Create and activate virtual environment**

   On Windows (PowerShell):

   ```powershell
   python -m venv venv
   .\\venv\\Scripts\\Activate.ps1
   ```

   On Windows (cmd):

   ```cmd
   python -m venv venv
   venv\\Scripts\\activate
   ```

   On macOS / Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Run development server**

```bash
python manage.py runserver
```

## 📁 Project Structure

django-blog/
├── blog/ # Main blog application
│ ├── models.py # Database models (Post, Category, Comment)
│ ├── views.py # View functions
│ ├── urls.py # URL routes
│ ├── admin.py # Admin panel configuration
└── templates/ # Blog templates
├── personal_blog/ # Project configuration
│ └── settings.py # Django settings
├── templates/ # Base templates
├── static/ # Static files (CSS, JS, images)
└── manage.py # Django management script

## 🎨 Customization

- Styling: Modify Tailwind classes in templates

- Models: Add new fields in `blog/models.py`

- Templates: Edit HTML files in the `templates/` directory

- Admin: Customize admin interface in `blog/admin.py`

## 🌍 Deployment

This project is configured for easy deployment on Render:

1. Push to GitHub
2. Connect repository to Render
3. Enable automatic deployments on pushes to the `main` branch

## 👨‍💻 Author

Eyob

GitHub: @eyob42

⭐ Star this repository if you found it helpful!
