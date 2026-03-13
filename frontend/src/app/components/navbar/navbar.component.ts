import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  template: `
    <nav class="bg-gradient-to-r from-red-to-pink-to-purple-horizontal shadow-lg">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <h1 class="text-white text-xl font-bold">AI Purchase</h1>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <a routerLink="/" routerLinkActive="bg-white bg-opacity-20"
               class="text-white hover:bg-white hover:bg-opacity-20 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200">
              Inicio
            </a>
            <a routerLink="/products" routerLinkActive="bg-white bg-opacity-20"
               class="text-white hover:bg-white hover:bg-opacity-20 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200">
              Productos
            </a>
          </div>
        </div>
      </div>
    </nav>
  `,
  styles: []
})
export class NavbarComponent {

}