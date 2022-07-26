import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

import { Device } from '../models/device.model';
import users from '../../users';

@Injectable({
  providedIn: 'root'
})
export class DeviceService {
  baseUrl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  // http headers
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  // POST
  CreateDevice(data: any): Observable<Device> {
    return this.http.post<Device>(
      `${this.baseUrl}api/devices/client/${users.getLuluWright().id}/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetClientDevices(): Observable<Device>{
    return this.http.get<Device>(`${this.baseUrl}api/devices/client/${users.getLuluWright().id}/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetDevice(id: number): Observable<Device> {
    return this.http.get<Device>(`${this.baseUrl}api/devices/${id}/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetDevices(): Observable<Device> {
    return this.http.get<Device>(`${this.baseUrl}api/devices/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // PUT
  UpdateDevice(id: number, data: any): Observable<Device> {
    return this.http.put<Device>(
      `${this.baseUrl}api/devices/${id}/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // DELETE
  DeleteDevice(id: number): Observable<Device> {
    return this.http.delete<Device>(`${this.baseUrl}api/devices/${id}/`, this.httpOptions)
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
