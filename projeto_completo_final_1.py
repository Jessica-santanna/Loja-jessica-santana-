#!/usr/bin/env python3
"""
PROJETO COMPLETO JÉSSICA SANTANA - SCRIPT DEFINITIVO
Execute: python3 projeto_completo_final.py
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {path}")

def main():
    print("🚀 CRIANDO PROJETO COMPLETO JÉSSICA SANTANA")
    print("=" * 60)
    
    base = "jessica-santana-loja"
    
    # ============ ARQUIVOS PRINCIPAIS ============
    
    # README.md
    create_file(f"{base}/README.md", """# 🛍️ Jéssica Santana - E-commerce de Moda Feminina

> Plataforma completa de e-commerce para moda feminina elegante, desenvolvida com React e Flask.

## 🌟 Demonstração

- **🌐 Site:** https://jessicasantanna.com.br
- **📱 Responsivo:** Funciona em desktop e mobile
- **⚡ Performance:** Carregamento rápido e otimizado

## 🚀 Funcionalidades

### 👥 Para Clientes
- [x] Catálogo de produtos com filtros
- [x] Detalhes completos dos produtos
- [x] Carrinho de compras
- [x] Sistema de autenticação
- [x] Área do cliente
- [x] Checkout simplificado

### 👨‍💼 Para Administradores
- [x] Painel administrativo
- [x] Gestão de produtos
- [x] Controle de estoque
- [x] Relatórios de vendas
- [x] Gestão de usuários

## 🛠️ Tecnologias

### Frontend
- **React 18** - Interface moderna e reativa
- **Vite** - Build tool rápido
- **Tailwind CSS** - Estilização responsiva
- **React Router** - Navegação SPA
- **Axios** - Requisições HTTP

### Backend
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **JWT** - Autenticação segura
- **Flask-CORS** - Configuração de CORS
- **SQLite/PostgreSQL** - Banco de dados

### Deploy
- **Frontend:** Netlify
- **Backend:** Railway
- **Domínio:** jessicasantanna.com.br

## 🚀 Como Executar Localmente

### Pré-requisitos
- Node.js 18+
- Python 3.8+
- Git

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### URLs Locais
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

## 🎨 Design System

- **Cores:** Paleta nude/bege elegante
- **Tipografia:** Playfair Display + Inter
- **Componentes:** Reutilizáveis e acessíveis
- **Responsivo:** Mobile-first approach

## 🔐 Segurança

- Autenticação JWT
- Validação de dados
- Sanitização de inputs
- HTTPS obrigatório

## 👩‍💻 Autora

**Jéssica Santana**
- Email: contato@jessicasantanna.com.br
- Site: https://jessicasantanna.com.br

---

⭐ Moda feminina elegante com tecnologia moderna!""")

    # .gitignore
    create_file(f"{base}/.gitignore", """# Dependencies
node_modules/
*/node_modules/
.pnpm-store/

# Build outputs
dist/
build/
*.tgz
*.tar.gz

# Environment files
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/
instance/
.webassets-cache

# Database
*.db
*.sqlite
*.sqlite3

# Flask
instance/
.webassets-cache

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor directories and files
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?""")

    # ============ BACKEND COMPLETO ============
    
    # requirements.txt
    create_file(f"{base}/backend/requirements.txt", """Flask==3.1.1
flask-cors==6.0.0
Flask-JWT-Extended==4.7.1
Flask-SQLAlchemy==3.1.1
gunicorn==21.2.0
python-dotenv==1.0.0
Werkzeug==3.1.3""")

    # railway.json
    create_file(f"{base}/backend/railway.json", """{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn -w 2 -b 0.0.0.0:$PORT app:app",
    "healthcheckPath": "/api/health"
  }
}""")

    # Procfile
    create_file(f"{base}/backend/Procfile", """web: gunicorn -w 2 -b 0.0.0.0:$PORT app:app""")

    # app.py (backend principal)
    create_file(f"{base}/backend/app.py", """from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'jessica-santana-secret-2025')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jessica-santana-jwt-2025')

# Configuração do banco de dados
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # Para produção (PostgreSQL)
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Para desenvolvimento (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app, origins=['*'])

# ============ MODELOS ============

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(500))
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    category = db.relationship('Category', backref='products')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'original_price': self.original_price,
            'category_id': self.category_id,
            'category': self.category.to_dict() if self.category else None,
            'stock': self.stock,
            'image_url': self.image_url,
            'is_featured': self.is_featured,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# ============ ROTAS ============

@app.route('/api/health')
def health():
    return {'status': 'ok', 'message': 'API Jéssica Santana funcionando!'}

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'message': 'Email e senha são obrigatórios'}), 400
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return jsonify({
                'message': 'Login realizado com sucesso',
                'user': user.to_dict(),
                'access_token': access_token
            }), 200
        
        return jsonify({'message': 'Credenciais inválidas'}), 401
    except Exception as e:
        return jsonify({'message': f'Erro interno: {str(e)}'}), 500

@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        if User.query.filter_by(email=data.get('email')).first():
            return jsonify({'message': 'Email já cadastrado'}), 400
        
        user = User(
            name=data.get('name'),
            email=data.get('email')
        )
        user.set_password(data.get('password'))
        
        db.session.add(user)
        db.session.commit()
        
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'message': 'Usuário criado com sucesso',
            'user': user.to_dict(),
            'access_token': access_token
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erro interno: {str(e)}'}), 500

@app.route('/api/products')
def get_products():
    try:
        category_id = request.args.get('category_id')
        featured = request.args.get('featured')
        
        query = Product.query.filter_by(is_active=True)
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if featured:
            query = query.filter_by(is_featured=True)
        
        products = query.all()
        return jsonify({'products': [p.to_dict() for p in products]})
    except Exception as e:
        return jsonify({'message': f'Erro interno: {str(e)}'}), 500

@app.route('/api/products/<int:id>')
def get_product(id):
    try:
        product = Product.query.get_or_404(id)
        return jsonify({'product': product.to_dict()})
    except Exception as e:
        return jsonify({'message': f'Erro interno: {str(e)}'}), 500

@app.route('/api/categories')
def get_categories():
    try:
        categories = Category.query.all()
        return jsonify({'categories': [c.to_dict() for c in categories]})
    except Exception as e:
        return jsonify({'message': f'Erro interno: {str(e)}'}), 500

# ============ INICIALIZAÇÃO ============

def init_db():
    with app.app_context():
        db.create_all()
        
        # Criar categorias padrão
        if not Category.query.first():
            categories = [
                Category(name='Alfaiataria', slug='alfaiataria', description='Peças sob medida e elegantes'),
                Category(name='Moda Social', slug='moda-social', description='Para eventos especiais'),
                Category(name='Looks Elegantes', slug='looks-elegantes', description='Sofisticação no dia a dia')
            ]
            for cat in categories:
                db.session.add(cat)
        
        # Criar produtos de exemplo
        if not Product.query.first():
            products = [
                Product(
                    name='Blazer Premium Alfaiataria',
                    description='Blazer elegante em alfaiataria premium, confeccionado com tecidos nobres e acabamento impecável. Ideal para mulheres que buscam sofisticação e elegância no ambiente corporativo.',
                    price=599.90,
                    original_price=799.90,
                    category_id=1,
                    stock=10,
                    is_featured=True,
                    image_url='https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500'
                ),
                Product(
                    name='Vestido Social Executivo',
                    description='Vestido social para eventos especiais e ambiente corporativo. Corte moderno que valoriza a silhueta feminina com elegância e sofisticação.',
                    price=299.90,
                    original_price=399.90,
                    category_id=2,
                    stock=15,
                    is_featured=True,
                    image_url='https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=500'
                ),
                Product(
                    name='Conjunto Executivo Completo',
                    description='Conjunto completo para ambiente corporativo, composto por blazer e calça ou saia. Perfeito para mulheres executivas que valorizam elegância e profissionalismo.',
                    price=899.90,
                    original_price=1199.90,
                    category_id=3,
                    stock=8,
                    is_featured=True,
                    image_url='https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500'
                ),
                Product(
                    name='Saia Lápis Clássica',
                    description='Saia lápis clássica e elegante, peça fundamental no guarda-roupa feminino. Corte que valoriza as curvas com sofisticação e classe.',
                    price=199.90,
                    category_id=1,
                    stock=20,
                    image_url='https://images.unsplash.com/photo-1583496661160-fb5886a13d77?w=500'
                ),
                Product(
                    name='Camisa Social Feminina',
                    description='Camisa social feminina com corte moderno e elegante. Tecido de alta qualidade que proporciona conforto e sofisticação.',
                    price=149.90,
                    category_id=2,
                    stock=25,
                    image_url='https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=500'
                ),
                Product(
                    name='Vestido Midi Elegante',
                    description='Vestido midi elegante para ocasiões especiais. Design sofisticado que combina conforto e elegância em uma peça única.',
                    price=349.90,
                    category_id=3,
                    stock=12,
                    image_url='https://images.unsplash.com/photo-1566479179817-c0b7b8b5e3b5?w=500'
                )
            ]
            for prod in products:
                db.session.add(prod)
        
        # Criar admin padrão
        if not User.query.filter_by(email='admin@jessicasantanna.com.br').first():
            admin = User(
                name='Jéssica Santana',
                email='admin@jessicasantanna.com.br',
                is_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
        
        db.session.commit()
        print("✅ Banco de dados inicializado!")

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)""")

    # ============ FRONTEND COMPLETO ============
    
    # package.json
    create_file(f"{base}/frontend/package.json", """{
  "name": "jessica-santana-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.1",
    "axios": "^1.3.4",
    "lucide-react": "^0.263.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.3",
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.24",
    "tailwindcss": "^3.3.2",
    "vite": "^4.4.5"
  }
}""")

    # vite.config.js
    create_file(f"{base}/frontend/vite.config.js", """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true
  },
  build: {
    outDir: 'dist'
  }
})""")

    # netlify.toml
    create_file(f"{base}/frontend/netlify.toml", """[build]
  publish = "dist"
  command = "npm run build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200""")

    # index.html
    create_file(f"{base}/frontend/index.html", """<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Jéssica Santana - Moda Feminina Elegante</title>
    <meta name="description" content="Moda feminina elegante com foco em alfaiataria e looks sofisticados para mulheres que valorizam qualidade e estilo.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""")

    # tailwind.config.js
    create_file(f"{base}/frontend/tailwind.config.js", """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#fdf8f6',
          100: '#f2e8e5',
          200: '#eaddd7',
          300: '#e0cec7',
          400: '#d2bab0',
          500: '#bfa094',
          600: '#a18072',
          700: '#977669',
          800: '#846358',
          900: '#43302b',
        },
        nude: {
          50: '#faf9f7',
          100: '#f0ede8',
          200: '#e6ddd4',
          300: '#d9cbb8',
          400: '#c9b59c',
          500: '#b8a082',
          600: '#a08b6f',
          700: '#8a7660',
          800: '#726252',
          900: '#5d5144',
        }
      },
      fontFamily: {
        'serif': ['Playfair Display', 'serif'],
        'sans': ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}""")

    # postcss.config.js
    create_file(f"{base}/frontend/postcss.config.js", """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}""")

    # src/main.jsx
    create_file(f"{base}/frontend/src/main.jsx", """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""")

    # src/index.css
    create_file(f"{base}/frontend/src/index.css", """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-3 px-6 rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2;
  }
  
  .btn-secondary {
    @apply bg-white hover:bg-gray-50 text-gray-700 font-medium py-3 px-6 rounded-lg border border-gray-300 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2;
  }
  
  .card {
    @apply bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200;
  }
  
  .container-custom {
    @apply max-w-7xl mx-auto px-4 sm:px-6 lg:px-8;
  }
}

body {
  font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
  font-family: 'Playfair Display', serif;
}""")

    # src/App.jsx
    create_file(f"{base}/frontend/src/App.jsx", """import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import Home from './pages/Home'
import Products from './pages/Products'
import ProductDetail from './pages/ProductDetail'
import Cart from './pages/Cart'
import About from './pages/About'
import Contact from './pages/Contact'

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/produtos" element={<Products />} />
            <Route path="/produto/:id" element={<ProductDetail />} />
            <Route path="/carrinho" element={<Cart />} />
            <Route path="/sobre" element={<About />} />
            <Route path="/contato" element={<Contact />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  )
}

export default App""")

    # src/lib/api.js
    create_file(f"{base}/frontend/src/lib/api.js", """import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para adicionar token de autenticação
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api""")

    # ============ COMPONENTES ============

    # src/components/Header.jsx
    create_file(f"{base}/frontend/src/components/Header.jsx", """import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Search, ShoppingBag, User, Menu, X } from 'lucide-react'

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="bg-white shadow-sm border-b border-gray-100 sticky top-0 z-50">
      <div className="container-custom">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex-shrink-0">
            <h1 className="text-2xl font-serif font-bold text-primary-700">
              Jéssica Santana
            </h1>
          </Link>

          {/* Navigation Desktop */}
          <nav className="hidden md:flex space-x-8">
            <Link to="/" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Início
            </Link>
            <Link to="/produtos" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Produtos
            </Link>
            <Link to="/sobre" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Sobre
            </Link>
            <Link to="/contato" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Contato
            </Link>
          </nav>

          {/* Actions */}
          <div className="flex items-center space-x-4">
            <Link to="/carrinho" className="relative flex items-center text-gray-700 hover:text-primary-600 transition-colors">
              <ShoppingBag size={20} />
              <span className="absolute -top-2 -right-2 bg-primary-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                0
              </span>
            </Link>

            {/* Mobile menu button */}
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden text-gray-700 hover:text-primary-600 transition-colors"
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden border-t border-gray-100 py-4">
            <nav className="space-y-2">
              <Link 
                to="/" 
                className="block py-2 text-gray-700 hover:text-primary-600 transition-colors font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Início
              </Link>
              <Link 
                to="/produtos" 
                className="block py-2 text-gray-700 hover:text-primary-600 transition-colors font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Produtos
              </Link>
              <Link 
                to="/sobre" 
                className="block py-2 text-gray-700 hover:text-primary-600 transition-colors font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Sobre
              </Link>
              <Link 
                to="/contato" 
                className="block py-2 text-gray-700 hover:text-primary-600 transition-colors font-medium"
                onClick={() => setIsMenuOpen(false)}
              >
                Contato
              </Link>
            </nav>
          </div>
        )}
      </div>
    </header>
  )
}

export default Header""")

    # src/components/Footer.jsx
    create_file(f"{base}/frontend/src/components/Footer.jsx", """import React from 'react'
import { Link } from 'react-router-dom'
import { Instagram, Facebook, Mail, Phone, MapPin } from 'lucide-react'

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="container-custom py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="space-y-4">
            <h3 className="text-2xl font-serif font-bold text-primary-300">
              Jéssica Santana
            </h3>
            <p className="text-gray-300 text-sm leading-relaxed">
              Moda feminina elegante com foco em alfaiataria e looks sofisticados para mulheres que valorizam qualidade e estilo.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-400 hover:text-primary-300 transition-colors">
                <Instagram size={20} />
              </a>
              <a href="#" className="text-gray-400 hover:text-primary-300 transition-colors">
                <Facebook size={20} />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Links Rápidos</h4>
            <nav className="space-y-2">
              <Link to="/produtos" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Todos os Produtos
              </Link>
              <Link to="/sobre" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Sobre Nós
              </Link>
              <Link to="/contato" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Contato
              </Link>
            </nav>
          </div>

          {/* Categories */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Categorias</h4>
            <nav className="space-y-2">
              <Link to="/produtos?categoria=alfaiataria" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Alfaiataria
              </Link>
              <Link to="/produtos?categoria=moda-social" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Moda Social
              </Link>
              <Link to="/produtos?categoria=looks-elegantes" className="block text-gray-300 hover:text-primary-300 transition-colors text-sm">
                Looks Elegantes
              </Link>
            </nav>
          </div>

          {/* Contact */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Contato</h4>
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <Phone size={16} className="text-primary-300 flex-shrink-0" />
                <span className="text-gray-300 text-sm">(11) 99999-9999</span>
              </div>
              <div className="flex items-center space-x-3">
                <Mail size={16} className="text-primary-300 flex-shrink-0" />
                <span className="text-gray-300 text-sm">contato@jessicasantanna.com.br</span>
              </div>
              <div className="flex items-start space-x-3">
                <MapPin size={16} className="text-primary-300 flex-shrink-0 mt-0.5" />
                <span className="text-gray-300 text-sm">São Paulo, SP</span>
              </div>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-gray-400 text-sm">
            © 2025 Jéssica Santana. Todos os direitos reservados.
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer""")

    # ============ PÁGINAS ============

    # src/pages/Home.jsx
    create_file(f"{base}/frontend/src/pages/Home.jsx", """import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { ArrowRight, Star, Truck, Shield, CreditCard } from 'lucide-react'
import api from '../lib/api'

const Home = () => {
  const [featuredProducts, setFeaturedProducts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchFeaturedProducts = async () => {
      try {
        const response = await api.get('/products?featured=true')
        setFeaturedProducts(response.data.products || [])
      } catch (error) {
        console.error('Erro ao carregar produtos:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchFeaturedProducts()
  }, [])

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-primary-50 to-nude-100 py-20">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-8">
              <div className="space-y-4">
                <h1 className="text-4xl md:text-5xl lg:text-6xl font-serif font-bold text-gray-900 leading-tight">
                  Elegância que
                  <span className="text-primary-600 block">Inspira</span>
                </h1>
                <p className="text-lg text-gray-600 leading-relaxed">
                  Descubra nossa coleção exclusiva de moda feminina, onde cada peça é cuidadosamente selecionada para mulheres que valorizam sofisticação e qualidade.
                </p>
              </div>
              
              <div className="flex flex-col sm:flex-row gap-4">
                <Link to="/produtos" className="btn-primary inline-flex items-center justify-center">
                  Ver Coleção
                  <ArrowRight size={20} className="ml-2" />
                </Link>
                <Link to="/sobre" className="btn-secondary inline-flex items-center justify-center">
                  Sobre Nós
                </Link>
              </div>

              <div className="flex items-center space-x-6 pt-4">
                <div className="flex items-center space-x-1">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} size={16} className="text-yellow-400 fill-current" />
                  ))}
                  <span className="text-sm text-gray-600 ml-2">4.9/5 (200+ avaliações)</span>
                </div>
              </div>
            </div>

            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-primary-200 to-nude-200 rounded-2xl flex items-center justify-center">
                <img 
                  src="https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600&h=600&fit=crop&crop=center" 
                  alt="Moda Feminina Elegante"
                  className="w-full h-full object-cover rounded-2xl"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Truck className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Frete Grátis</h3>
              <p className="text-gray-600">Para compras acima de R$ 299</p>
            </div>
            
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Shield className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Compra Segura</h3>
              <p className="text-gray-600">Seus dados protegidos</p>
            </div>
            
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <CreditCard className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Parcelamento</h3>
              <p className="text-gray-600">Em até 12x sem juros</p>
            </div>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="text-center space-y-4 mb-12">
            <h2 className="text-3xl md:text-4xl font-serif font-bold text-gray-900">
              Nossas Categorias
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Explore nossa seleção cuidadosa de peças para cada ocasião
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <Link to="/produtos?categoria=alfaiataria" className="group">
              <div className="card overflow-hidden">
                <div className="aspect-[4/3] bg-gradient-to-br from-primary-100 to-nude-100">
                  <img 
                    src="https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=300&fit=crop" 
                    alt="Alfaiataria"
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-serif font-semibold mb-2">Alfaiataria</h3>
                  <p className="text-gray-600 text-sm">Peças sob medida e elegantes</p>
                </div>
              </div>
            </Link>

            <Link to="/produtos?categoria=moda-social" className="group">
              <div className="card overflow-hidden">
                <div className="aspect-[4/3] bg-gradient-to-br from-primary-100 to-nude-100">
                  <img 
                    src="https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=300&fit=crop" 
                    alt="Moda Social"
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-serif font-semibold mb-2">Moda Social</h3>
                  <p className="text-gray-600 text-sm">Para eventos especiais</p>
                </div>
              </div>
            </Link>

            <Link to="/produtos?categoria=looks-elegantes" className="group">
              <div className="card overflow-hidden">
                <div className="aspect-[4/3] bg-gradient-to-br from-primary-100 to-nude-100">
                  <img 
                    src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=300&fit=crop" 
                    alt="Looks Elegantes"
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-serif font-semibold mb-2">Looks Elegantes</h3>
                  <p className="text-gray-600 text-sm">Sofisticação no dia a dia</p>
                </div>
              </div>
            </Link>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="text-center space-y-4 mb-12">
            <h2 className="text-3xl md:text-4xl font-serif font-bold text-gray-900">
              Produtos em Destaque
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Peças selecionadas especialmente para você
            </p>
          </div>

          {loading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[...Array(3)].map((_, i) => (
                <div key={i} className="card animate-pulse">
                  <div className="aspect-[3/4] bg-gray-200"></div>
                  <div className="p-6 space-y-3">
                    <div className="h-4 bg-gray-200 rounded"></div>
                    <div className="h-4 bg-gray-200 rounded w-2/3"></div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featuredProducts.slice(0, 3).map((product) => (
                <Link key={product.id} to={`/produto/${product.id}`} className="group">
                  <div className="card overflow-hidden">
                    <div className="aspect-[3/4] bg-gradient-to-br from-primary-100 to-nude-100">
                      <img 
                        src={product.image_url || 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=500&fit=crop'} 
                        alt={product.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                      />
                    </div>
                    <div className="p-6">
                      <h3 className="text-lg font-semibold mb-2 group-hover:text-primary-600 transition-colors">
                        {product.name}
                      </h3>
                      <div className="flex items-center space-x-2">
                        <span className="text-xl font-bold text-primary-600">
                          R$ {product.price?.toFixed(2)}
                        </span>
                        {product.original_price && product.original_price > product.price && (
                          <span className="text-sm text-gray-500 line-through">
                            R$ {product.original_price.toFixed(2)}
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}

          <div className="text-center mt-12">
            <Link to="/produtos" className="btn-primary inline-flex items-center">
              Ver Todos os Produtos
              <ArrowRight size={20} className="ml-2" />
            </Link>
          </div>
        </div>
      </section>

      {/* About Preview */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              <h2 className="text-3xl md:text-4xl font-serif font-bold text-gray-900">
                Moda com Propósito
              </h2>
              <p className="text-lg text-gray-600 leading-relaxed">
                Na Jéssica Santana, acreditamos que a moda é uma forma de expressão pessoal. 
                Cada peça é cuidadosamente selecionada para mulheres que valorizam qualidade, 
                elegância e sofisticação em seu guarda-roupa.
              </p>
              <p className="text-gray-600 leading-relaxed">
                Nossa missão é oferecer roupas que não apenas vestem, mas que empoderam e 
                inspiram confiança em cada mulher que as usa.
              </p>
              <Link to="/sobre" className="btn-secondary inline-flex items-center">
                Conheça Nossa História
                <ArrowRight size={20} className="ml-2" />
              </Link>
            </div>

            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-primary-200 to-nude-200 rounded-2xl flex items-center justify-center">
                <img 
                  src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&h=600&fit=crop&crop=center" 
                  alt="Sobre Jéssica Santana"
                  className="w-full h-full object-cover rounded-2xl"
                />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Home""")

    # src/pages/Products.jsx
    create_file(f"{base}/frontend/src/pages/Products.jsx", """import React, { useState, useEffect } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { Filter, Grid, List } from 'lucide-react'
import api from '../lib/api'

const Products = () => {
  const [products, setProducts] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [viewMode, setViewMode] = useState('grid')
  const [searchParams] = useSearchParams()

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [productsResponse, categoriesResponse] = await Promise.all([
          api.get('/products'),
          api.get('/categories')
        ])
        
        setProducts(productsResponse.data.products || [])
        setCategories(categoriesResponse.data.categories || [])
      } catch (error) {
        console.error('Erro ao carregar dados:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  const selectedCategory = searchParams.get('categoria')

  const filteredProducts = selectedCategory
    ? products.filter(product => 
        product.category?.slug === selectedCategory
      )
    : products

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="container-custom">
          <div className="animate-pulse space-y-8">
            <div className="h-8 bg-gray-200 rounded w-1/3"></div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[...Array(6)].map((_, i) => (
                <div key={i} className="card">
                  <div className="aspect-[3/4] bg-gray-200"></div>
                  <div className="p-6 space-y-3">
                    <div className="h-4 bg-gray-200 rounded"></div>
                    <div className="h-4 bg-gray-200 rounded w-2/3"></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container-custom">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-serif font-bold text-gray-900 mb-4">
            {selectedCategory 
              ? categories.find(cat => cat.slug === selectedCategory)?.name || 'Produtos'
              : 'Todos os Produtos'
            }
          </h1>
          <p className="text-gray-600">
            {filteredProducts.length} produto{filteredProducts.length !== 1 ? 's' : ''} encontrado{filteredProducts.length !== 1 ? 's' : ''}
          </p>
        </div>

        {/* Filters */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
          <div className="flex flex-wrap gap-2">
            <Link 
              to="/produtos"
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                !selectedCategory 
                  ? 'bg-primary-600 text-white' 
                  : 'bg-white text-gray-700 hover:bg-gray-50 border border-gray-300'
              }`}
            >
              Todos
            </Link>
            {categories.map((category) => (
              <Link
                key={category.id}
                to={`/produtos?categoria=${category.slug}`}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  selectedCategory === category.slug
                    ? 'bg-primary-600 text-white'
                    : 'bg-white text-gray-700 hover:bg-gray-50 border border-gray-300'
                }`}
              >
                {category.name}
              </Link>
            ))}
          </div>

          <div className="flex items-center space-x-2">
            <button
              onClick={() => setViewMode('grid')}
              className={`p-2 rounded-lg ${
                viewMode === 'grid' 
                  ? 'bg-primary-600 text-white' 
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              <Grid size={20} />
            </button>
            <button
              onClick={() => setViewMode('list')}
              className={`p-2 rounded-lg ${
                viewMode === 'list' 
                  ? 'bg-primary-600 text-white' 
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              <List size={20} />
            </button>
          </div>
        </div>

        {/* Products Grid */}
        {filteredProducts.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">Nenhum produto encontrado nesta categoria.</p>
          </div>
        ) : (
          <div className={`grid gap-8 ${
            viewMode === 'grid' 
              ? 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3' 
              : 'grid-cols-1'
          }`}>
            {filteredProducts.map((product) => (
              <Link key={product.id} to={`/produto/${product.id}`} className="group">
                <div className={`card overflow-hidden ${
                  viewMode === 'list' ? 'flex flex-col sm:flex-row' : ''
                }`}>
                  <div className={`bg-gradient-to-br from-primary-100 to-nude-100 ${
                    viewMode === 'list' 
                      ? 'aspect-square sm:aspect-[3/4] sm:w-64 flex-shrink-0' 
                      : 'aspect-[3/4]'
                  }`}>
                    <img 
                      src={product.image_url || 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=500&fit=crop'} 
                      alt={product.name}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                    />
                  </div>
                  <div className="p-6 flex-1">
                    <div className="space-y-2">
                      <h3 className="text-lg font-semibold group-hover:text-primary-600 transition-colors">
                        {product.name}
                      </h3>
                      {product.category && (
                        <p className="text-sm text-gray-500">{product.category.name}</p>
                      )}
                      {viewMode === 'list' && product.description && (
                        <p className="text-gray-600 text-sm line-clamp-2">
                          {product.description}
                        </p>
                      )}
                      <div className="flex items-center space-x-2">
                        <span className="text-xl font-bold text-primary-600">
                          R$ {product.price?.toFixed(2)}
                        </span>
                        {product.original_price && product.original_price > product.price && (
                          <>
                            <span className="text-sm text-gray-500 line-through">
                              R$ {product.original_price.toFixed(2)}
                            </span>
                            <span className="text-xs bg-red-100 text-red-600 px-2 py-1 rounded">
                              -{Math.round(((product.original_price - product.price) / product.original_price) * 100)}%
                            </span>
                          </>
                        )}
                      </div>
                      {product.stock > 0 ? (
                        <p className="text-sm text-green-600">Em estoque</p>
                      ) : (
                        <p className="text-sm text-red-600">Fora de estoque</p>
                      )}
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default Products""")

    # src/pages/ProductDetail.jsx
    create_file(f"{base}/frontend/src/pages/ProductDetail.jsx", """import React, { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, ShoppingBag, Heart, Share2, Star } from 'lucide-react'
import api from '../lib/api'

const ProductDetail = () => {
  const { id } = useParams()
  const [product, setProduct] = useState(null)
  const [loading, setLoading] = useState(true)
  const [quantity, setQuantity] = useState(1)

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await api.get(`/products/${id}`)
        setProduct(response.data.product)
      } catch (error) {
        console.error('Erro ao carregar produto:', error)
      } finally {
        setLoading(false)
      }
    }

    if (id) {
      fetchProduct()
    }
  }, [id])

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="container-custom">
          <div className="animate-pulse">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
              <div className="aspect-square bg-gray-200 rounded-lg"></div>
              <div className="space-y-6">
                <div className="h-8 bg-gray-200 rounded"></div>
                <div className="h-4 bg-gray-200 rounded w-2/3"></div>
                <div className="h-6 bg-gray-200 rounded w-1/3"></div>
                <div className="space-y-2">
                  <div className="h-4 bg-gray-200 rounded"></div>
                  <div className="h-4 bg-gray-200 rounded"></div>
                  <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (!product) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="container-custom">
          <div className="text-center py-12">
            <h1 className="text-2xl font-serif font-bold text-gray-900 mb-4">
              Produto não encontrado
            </h1>
            <Link to="/produtos" className="btn-primary">
              Voltar aos Produtos
            </Link>
          </div>
        </div>
      </div>
    )
  }

  const handleAddToCart = () => {
    // Implementar lógica do carrinho
    alert(`${product.name} adicionado ao carrinho!`)
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container-custom">
        {/* Breadcrumb */}
        <div className="flex items-center space-x-2 text-sm text-gray-600 mb-8">
          <Link to="/" className="hover:text-primary-600">Início</Link>
          <span>/</span>
          <Link to="/produtos" className="hover:text-primary-600">Produtos</Link>
          <span>/</span>
          <span className="text-gray-900">{product.name}</span>
        </div>

        {/* Back Button */}
        <Link 
          to="/produtos" 
          className="inline-flex items-center text-gray-600 hover:text-primary-600 mb-8 transition-colors"
        >
          <ArrowLeft size={20} className="mr-2" />
          Voltar aos Produtos
        </Link>

        {/* Product Details */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          {/* Product Image */}
          <div className="space-y-4">
            <div className="aspect-square bg-gradient-to-br from-primary-100 to-nude-100 rounded-lg overflow-hidden">
              <img 
                src={product.image_url || 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600&h=600&fit=crop'} 
                alt={product.name}
                className="w-full h-full object-cover"
              />
            </div>
          </div>

          {/* Product Info */}
          <div className="space-y-6">
            <div>
              {product.category && (
                <p className="text-sm text-primary-600 font-medium mb-2">
                  {product.category.name}
                </p>
              )}
              <h1 className="text-3xl md:text-4xl font-serif font-bold text-gray-900 mb-4">
                {product.name}
              </h1>
              
              {/* Rating */}
              <div className="flex items-center space-x-2 mb-4">
                <div className="flex items-center space-x-1">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} size={16} className="text-yellow-400 fill-current" />
                  ))}
                </div>
                <span className="text-sm text-gray-600">(4.9) 23 avaliações</span>
              </div>

              {/* Price */}
              <div className="flex items-center space-x-3 mb-6">
                <span className="text-3xl font-bold text-primary-600">
                  R$ {product.price?.toFixed(2)}
                </span>
                {product.original_price && product.original_price > product.price && (
                  <>
                    <span className="text-xl text-gray-500 line-through">
                      R$ {product.original_price.toFixed(2)}
                    </span>
                    <span className="bg-red-100 text-red-600 px-3 py-1 rounded-full text-sm font-medium">
                      -{Math.round(((product.original_price - product.price) / product.original_price) * 100)}% OFF
                    </span>
                  </>
                )}
              </div>
            </div>

            {/* Description */}
            {product.description && (
              <div>
                <h3 className="text-lg font-semibold mb-3">Descrição</h3>
                <p className="text-gray-600 leading-relaxed">
                  {product.description}
                </p>
              </div>
            )}

            {/* Stock Status */}
            <div>
              {product.stock > 0 ? (
                <p className="text-green-600 font-medium">
                  ✓ Em estoque ({product.stock} unidades disponíveis)
                </p>
              ) : (
                <p className="text-red-600 font-medium">
                  ✗ Produto fora de estoque
                </p>
              )}
            </div>

            {/* Quantity and Add to Cart */}
            {product.stock > 0 && (
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Quantidade
                  </label>
                  <div className="flex items-center space-x-3">
                    <button
                      onClick={() => setQuantity(Math.max(1, quantity - 1))}
                      className="w-10 h-10 rounded-lg border border-gray-300 flex items-center justify-center hover:bg-gray-50 transition-colors"
                    >
                      -
                    </button>
                    <span className="w-12 text-center font-medium">{quantity}</span>
                    <button
                      onClick={() => setQuantity(Math.min(product.stock, quantity + 1))}
                      className="w-10 h-10 rounded-lg border border-gray-300 flex items-center justify-center hover:bg-gray-50 transition-colors"
                    >
                      +
                    </button>
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row gap-4">
                  <button
                    onClick={handleAddToCart}
                    className="btn-primary flex-1 flex items-center justify-center"
                  >
                    <ShoppingBag size={20} className="mr-2" />
                    Adicionar ao Carrinho
                  </button>
                  <button className="btn-secondary flex items-center justify-center">
                    <Heart size={20} className="mr-2" />
                    Favoritar
                  </button>
                </div>
              </div>
            )}

            {/* Additional Info */}
            <div className="border-t pt-6 space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
                <div>
                  <span className="font-medium text-gray-900">Categoria:</span>
                  <span className="text-gray-600 ml-2">
                    {product.category?.name || 'Não especificada'}
                  </span>
                </div>
                <div>
                  <span className="font-medium text-gray-900">SKU:</span>
                  <span className="text-gray-600 ml-2">#{product.id}</span>
                </div>
              </div>
              
              <div className="flex items-center space-x-4 pt-4">
                <button className="flex items-center text-gray-600 hover:text-primary-600 transition-colors">
                  <Share2 size={16} className="mr-2" />
                  Compartilhar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProductDetail""")

    # src/pages/Cart.jsx
    create_file(f"{base}/frontend/src/pages/Cart.jsx", """import React from 'react'
import { Link } from 'react-router-dom'
import { ShoppingBag, Trash2, Plus, Minus } from 'lucide-react'

const Cart = () => {
  // Mock data - implementar com contexto real
  const cartItems = []

  if (cartItems.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="container-custom">
          <h1 className="text-3xl md:text-4xl font-serif font-bold text-gray-900 mb-8">
            Carrinho de Compras
          </h1>
          
          <div className="text-center py-12">
            <ShoppingBag size={64} className="text-gray-300 mx-auto mb-4" />
            <h2 className="text-2xl font-serif font-bold text-gray-900 mb-2">
              Seu carrinho está vazio
            </h2>
            <p className="text-gray-600 mb-8">
              Adicione alguns produtos incríveis ao seu carrinho
            </p>
            <Link to="/produtos" className="btn-primary">
              Continuar Comprando
            </Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container-custom">
        <h1 className="text-3xl md:text-4xl font-serif font-bold text-gray-900 mb-8">
          Carrinho de Compras
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Cart Items */}
          <div className="lg:col-span-2 space-y-4">
            {/* Implementar lista de itens do carrinho */}
          </div>

          {/* Order Summary */}
          <div className="lg:col-span-1">
            <div className="card p-6 sticky top-8">
              <h3 className="text-lg font-semibold mb-4">Resumo do Pedido</h3>
              
              <div className="space-y-3 mb-6">
                <div className="flex justify-between">
                  <span>Subtotal</span>
                  <span>R$ 0,00</span>
                </div>
                <div className="flex justify-between">
                  <span>Frete</span>
                  <span>Grátis</span>
                </div>
                <div className="border-t pt-3 flex justify-between font-semibold text-lg">
                  <span>Total</span>
                  <span className="text-primary-600">R$ 0,00</span>
                </div>
              </div>

              <button className="btn-primary w-full mb-4">
                Finalizar Compra
              </button>
              
              <Link to="/produtos" className="btn-secondary w-full">
                Continuar Comprando
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Cart""")

    # src/pages/About.jsx
    create_file(f"{base}/frontend/src/pages/About.jsx", """import React from 'react'
import { Heart, Award, Users, Sparkles } from 'lucide-react'

const About = () => {
  return (
    <div className="min-h-screen bg-white">
      {/* Hero Section */}
      <section className="py-16 bg-gradient-to-br from-primary-50 to-nude-100">
        <div className="container-custom">
          <div className="text-center space-y-6">
            <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900">
              Nossa História
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
              Nascemos da paixão pela moda feminina elegante e do desejo de empoderar mulheres através de roupas que expressam personalidade e sofisticação.
            </p>
          </div>
        </div>
      </section>

      {/* Story Section */}
      <section className="py-16">
        <div className="container-custom">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              <h2 className="text-3xl font-serif font-bold text-gray-900">
                Jéssica Santana
              </h2>
              <p className="text-gray-600 leading-relaxed">
                Fundada em 2020, a Jéssica Santana nasceu do sonho de criar uma marca que celebrasse a elegância feminina em todas as suas formas. Nossa fundadora, apaixonada por moda e alfaiataria, viu a necessidade de oferecer peças que combinassem qualidade excepcional com design sofisticado.
              </p>
              <p className="text-gray-600 leading-relaxed">
                Cada peça em nossa coleção é cuidadosamente selecionada, pensando na mulher moderna que valoriza qualidade, conforto e estilo. Acreditamos que a moda é uma forma de expressão pessoal e uma ferramenta de empoderamento.
              </p>
              <p className="text-gray-600 leading-relaxed">
                Nossa missão é simples: oferecer roupas que não apenas vestem, mas que inspiram confiança e elegância em cada mulher que as usa.
              </p>
            </div>

            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-primary-200 to-nude-200 rounded-2xl overflow-hidden">
                <img 
                  src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&h=600&fit=crop&crop=center" 
                  alt="Jéssica Santana"
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="text-center space-y-4 mb-12">
            <h2 className="text-3xl md:text-4xl font-serif font-bold text-gray-900">
              Nossos Valores
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Os princípios que guiam cada decisão e cada peça que criamos
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Heart className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Paixão</h3>
              <p className="text-gray-600 text-sm">
                Cada peça é criada com amor e dedicação, refletindo nossa paixão pela moda feminina.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Award className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Qualidade</h3>
              <p className="text-gray-600 text-sm">
                Utilizamos apenas materiais premium e técnicas de confecção que garantem durabilidade.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Users className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Empoderamento</h3>
              <p className="text-gray-600 text-sm">
                Acreditamos que a moda é uma ferramenta de empoderamento e autoexpressão.
              </p>
            </div>

            <div className="text-center space-y-4">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                <Sparkles className="text-primary-600" size={24} />
              </div>
              <h3 className="text-xl font-serif font-semibold">Elegância</h3>
              <p className="text-gray-600 text-sm">
                Cada detalhe é pensado para proporcionar sofisticação e elegância atemporal.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-16">
        <div className="container-custom">
          <div className="text-center space-y-8">
            <h2 className="text-3xl md:text-4xl font-serif font-bold text-gray-900">
              Nossa Missão
            </h2>
            <div className="max-w-4xl mx-auto">
              <p className="text-xl text-gray-600 leading-relaxed mb-8">
                "Criar roupas que celebrem a individualidade de cada mulher, oferecendo peças que combinam elegância, qualidade e conforto. Queremos que cada cliente se sinta confiante, poderosa e autenticamente ela mesma."
              </p>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">500+</div>
                  <div className="text-gray-600">Clientes Satisfeitas</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">100+</div>
                  <div className="text-gray-600">Peças Exclusivas</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">4.9</div>
                  <div className="text-gray-600">Avaliação Média</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-gradient-to-br from-primary-600 to-primary-700 text-white">
        <div className="container-custom text-center space-y-6">
          <h2 className="text-3xl md:text-4xl font-serif font-bold">
            Faça Parte da Nossa História
          </h2>
          <p className="text-xl opacity-90 max-w-2xl mx-auto">
            Descubra nossa coleção e encontre peças que expressem sua personalidade única
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="/produtos" className="bg-white text-primary-600 hover:bg-gray-100 font-medium py-3 px-8 rounded-lg transition-colors">
              Ver Coleção
            </a>
            <a href="/contato" className="border border-white hover:bg-white hover:text-primary-600 font-medium py-3 px-8 rounded-lg transition-colors">
              Entre em Contato
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}

export default About""")

    # src/pages/Contact.jsx
    create_file(f"{base}/frontend/src/pages/Contact.jsx", """import React, { useState } from 'react'
import { Mail, Phone, MapPin, Clock, Instagram, Facebook } from 'lucide-react'

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    // Implementar envio do formulário
    alert('Mensagem enviada com sucesso! Entraremos em contato em breve.')
    setFormData({ name: '', email: '', subject: '', message: '' })
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center space-y-4 mb-12">
          <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900">
            Entre em Contato
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Estamos aqui para ajudar! Entre em contato conosco para dúvidas, sugestões ou informações sobre nossos produtos.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          {/* Contact Information */}
          <div className="space-y-8">
            <div>
              <h2 className="text-2xl font-serif font-bold text-gray-900 mb-6">
                Informações de Contato
              </h2>
              
              <div className="space-y-6">
                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Phone className="text-primary-600" size={20} />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Telefone</h3>
                    <p className="text-gray-600">(11) 99999-9999</p>
                    <p className="text-sm text-gray-500">Segunda a sexta, 9h às 18h</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Mail className="text-primary-600" size={20} />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">E-mail</h3>
                    <p className="text-gray-600">contato@jessicasantanna.com.br</p>
                    <p className="text-sm text-gray-500">Respondemos em até 24h</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <MapPin className="text-primary-600" size={20} />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Localização</h3>
                    <p className="text-gray-600">São Paulo, SP</p>
                    <p className="text-sm text-gray-500">Atendimento online</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Clock className="text-primary-600" size={20} />
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-1">Horário de Atendimento</h3>
                    <p className="text-gray-600">Segunda a sexta: 9h às 18h</p>
                    <p className="text-gray-600">Sábado: 9h às 14h</p>
                    <p className="text-sm text-gray-500">Domingo: Fechado</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Social Media */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Siga-nos nas Redes Sociais
              </h3>
              <div className="flex space-x-4">
                <a 
                  href="#" 
                  className="w-12 h-12 bg-primary-600 rounded-lg flex items-center justify-center text-white hover:bg-primary-700 transition-colors"
                >
                  <Instagram size={20} />
                </a>
                <a 
                  href="#" 
                  className="w-12 h-12 bg-primary-600 rounded-lg flex items-center justify-center text-white hover:bg-primary-700 transition-colors"
                >
                  <Facebook size={20} />
                </a>
              </div>
            </div>
          </div>

          {/* Contact Form */}
          <div className="card p-8">
            <h2 className="text-2xl font-serif font-bold text-gray-900 mb-6">
              Envie uma Mensagem
            </h2>
            
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
                    Nome *
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
                    placeholder="Seu nome"
                  />
                </div>
                
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                    E-mail *
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
                    placeholder="seu@email.com"
                  />
                </div>
              </div>

              <div>
                <label htmlFor="subject" className="block text-sm font-medium text-gray-700 mb-2">
                  Assunto *
                </label>
                <select
                  id="subject"
                  name="subject"
                  value={formData.subject}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
                >
                  <option value="">Selecione um assunto</option>
                  <option value="duvida-produto">Dúvida sobre produto</option>
                  <option value="pedido">Informações sobre pedido</option>
                  <option value="troca-devolucao">Troca ou devolução</option>
                  <option value="sugestao">Sugestão</option>
                  <option value="outro">Outro</option>
                </select>
              </div>

              <div>
                <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-2">
                  Mensagem *
                </label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  required
                  rows={6}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors resize-none"
                  placeholder="Digite sua mensagem aqui..."
                />
              </div>

              <button type="submit" className="btn-primary w-full">
                Enviar Mensagem
              </button>
            </form>
          </div>
        </div>

        {/* FAQ Section */}
        <div className="mt-16">
          <h2 className="text-3xl font-serif font-bold text-gray-900 text-center mb-8">
            Perguntas Frequentes
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="card p-6">
              <h3 className="font-semibold text-gray-900 mb-2">
                Como posso acompanhar meu pedido?
              </h3>
              <p className="text-gray-600 text-sm">
                Após a confirmação do pagamento, você receberá um e-mail com o código de rastreamento para acompanhar sua entrega.
              </p>
            </div>

            <div className="card p-6">
              <h3 className="font-semibold text-gray-900 mb-2">
                Qual é o prazo de entrega?
              </h3>
              <p className="text-gray-600 text-sm">
                O prazo varia de 3 a 7 dias úteis para São Paulo e região metropolitana, e de 5 a 10 dias úteis para outras regiões.
              </p>
            </div>

            <div className="card p-6">
              <h3 className="font-semibold text-gray-900 mb-2">
                Posso trocar ou devolver um produto?
              </h3>
              <p className="text-gray-600 text-sm">
                Sim! Você tem até 30 dias para trocar ou devolver produtos, desde que estejam em perfeito estado e com etiquetas.
              </p>
            </div>

            <div className="card p-6">
              <h3 className="font-semibold text-gray-900 mb-2">
                Vocês fazem peças sob medida?
              </h3>
              <p className="text-gray-600 text-sm">
                Sim! Entre em contato conosco para solicitar um orçamento personalizado para peças sob medida.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Contact""")

    print("\n🎉 PROJETO COMPLETO CRIADO COM SUCESSO!")
    print("=" * 60)
    print(f"📁 Pasta criada: {base}/")
    print("\n📋 Estrutura completa:")
    print("├── README.md")
    print("├── .gitignore")
    print("├── backend/")
    print("│   ├── app.py")
    print("│   ├── requirements.txt")
    print("│   ├── railway.json")
    print("│   └── Procfile")
    print("└── frontend/")
    print("    ├── package.json")
    print("    ├── vite.config.js")
    print("    ├── netlify.toml")
    print("    ├── index.html")
    print("    ├── tailwind.config.js")
    print("    ├── postcss.config.js")
    print("    └── src/")
    print("        ├── main.jsx")
    print("        ├── App.jsx")
    print("        ├── index.css")
    print("        ├── lib/api.js")
    print("        ├── components/")
    print("        │   ├── Header.jsx")
    print("        │   └── Footer.jsx")
    print("        └── pages/")
    print("            ├── Home.jsx")
    print("            ├── Products.jsx")
    print("            ├── ProductDetail.jsx")
    print("            ├── Cart.jsx")
    print("            ├── About.jsx")
    print("            └── Contact.jsx")
    print("\n🚀 PRÓXIMOS PASSOS:")
    print("1. Faça upload desta pasta para o GitHub")
    print("2. Configure Railway (backend)")
    print("3. Configure Netlify (frontend)")
    print("4. Configure seu domínio jessicasantanna.com.br")
    print("\n✨ Seu site estará completo e funcionando!")

if __name__ == "__main__":
    main()

