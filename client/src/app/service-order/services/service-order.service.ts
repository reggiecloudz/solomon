import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

import { ServiceOrder } from '../models/service-order.model';
import users from '../../shared/users';


@Injectable({
  providedIn: 'root'
})
export class ServiceOrderService {
  baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  // http headers
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  // POST
  CreateServiceOrder(data: any, id: number): Observable<ServiceOrder> {
    return this.http.post<ServiceOrder>(
      `${this.baseUrl}/service-orders/device/${id}/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetDeviceServiceOrders(id: number): Observable<ServiceOrder>{
    return this.http.get<ServiceOrder>(`${this.baseUrl}/service-orders/device/${id}/`,)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetServiceOrder(id: number): Observable<ServiceOrder> {
    return this.http.get<ServiceOrder>(`${this.baseUrl}/service-orders/${id}/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetServiceOrders(): Observable<ServiceOrder> {
    return this.http.get<ServiceOrder>(`${this.baseUrl}/service-orders/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  UpdateServiceOrder(id: number, data: any): Observable<ServiceOrder> {
    return this.http.put<ServiceOrder>(
      `${this.baseUrl}/service-orders/${id}/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // DELETE
  DeleteServiceOrder(id: number): Observable<ServiceOrder> {
    return this.http.delete<ServiceOrder>(`${this.baseUrl}/service-orders/${id}/`, this.httpOptions)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  errorHandler(error: any) {
    let errorMessage = '';

    if (error.error instanceof ErrorEvent) {
      // get client-side error
      errorMessage = error.error.message;
    }
    else {
      // get server-side error
      errorMessage = `Error code: ${error.status}\nMessage: ${error.message}`;
    }

    return throwError(() => {
      return errorMessage
    });
  }
}
