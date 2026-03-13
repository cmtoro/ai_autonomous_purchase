import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, of } from 'rxjs';
import { environment } from '../../environments/environment.prod';
import { Product } from '../models/product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private apiUrl = `${environment.apiUrl}/api/v1`;

  constructor(private http: HttpClient) { }

  getProducts(): Observable<Product[]> {
    console.log('Fetching products from API:', this.apiUrl);
    return this.http.get<Product[]>(`${this.apiUrl}/products`)
      .pipe(
        catchError(error => {
          console.error('Error fetching products:', error);
          return of([]);
        })
      );
  }
}