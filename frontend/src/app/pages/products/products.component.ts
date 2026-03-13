import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductService } from '../../services/product.service';
import { Product } from '../../models/product';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="min-h-screen bg-gray-50 py-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Nuestros Productos</h1>
          <p class="text-gray-600">Descubre nuestra selección de productos de calidad</p>
        </div>

        <div *ngIf="loading()" class="flex justify-center items-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-electric-violet"></div>
        </div>

        <div *ngIf="error()" class="text-center py-12">
          <div class="bg-red-50 border border-red-200 rounded-lg p-6 max-w-md mx-auto">
            <h3 class="text-red-800 font-medium mb-2">Error al cargar productos</h3>
            <p class="text-red-600 text-sm">No se pudieron cargar los productos. Inténtalo de nuevo más tarde.</p>
          </div>
        </div>

        <div *ngIf="!loading() && !error()" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div *ngFor="let product of products()" class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 overflow-hidden">
            <div class="p-6">
              <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ product.name }}</h3>
              <p class="text-2xl font-bold text-electric-violet mb-4">${{ product.price.toFixed(2) }}</p>
              <button class="w-full bg-gradient-to-r from-electric-violet to-french-violet text-white py-2 px-4 rounded-md hover:from-french-violet hover:to-electric-violet transition-all duration-200 font-medium">
                Ver detalles
              </button>
            </div>
          </div>
        </div>

        <div *ngIf="!loading() && !error() && products().length === 0" class="text-center py-12">
          <div class="bg-gray-50 border border-gray-200 rounded-lg p-6 max-w-md mx-auto">
            <h3 class="text-gray-800 font-medium mb-2">No hay productos disponibles</h3>
            <p class="text-gray-600 text-sm">Actualmente no tenemos productos en inventario.</p>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: []
})
export class ProductsComponent {
  private productService = inject(ProductService);

  products = signal<Product[]>([]);
  loading = signal<boolean>(true);
  error = signal<boolean>(false);

  constructor() {
    this.loadProducts();
  }

  private loadProducts() {
    this.loading.set(true);
    this.error.set(false);

    this.productService.getProducts().subscribe({
      next: (products) => {
        this.products.set(products);
        this.loading.set(false);
      },
      error: () => {
        this.error.set(true);
        this.loading.set(false);
      }
    });
  }
}