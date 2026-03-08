import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { environment } from '../environments/environment.prod';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected readonly title = signal('purchase-app');
  protected backendStatus = signal('unknown');

  constructor() {
    this.checkBackendStatus();
  }

  private async checkBackendStatus() {
    try {
      const statusUrl = new URL('/api/v1/health', environment.apiUrl).toString();
      const response = await fetch(statusUrl);
      if (response.ok) {
        this.backendStatus.set('healthy');
      } else {
        this.backendStatus.set('unhealthy');
      }
    } catch (error) {
      this.backendStatus.set('unreachable');
    }
  }
}
