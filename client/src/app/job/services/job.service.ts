import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

import { Job } from '../models/job.model';
import { ServiceOrder } from '../../service-order/models/service-order.model';

@Injectable({
  providedIn: 'root'
})
export class JobService {
  baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  // http headers
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  // POST
  CreateJob(data: any, id: number): Observable<Job> {
    return this.http.post<Job>(
      `${this.baseUrl}/jobs/service-order/${id}/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetJob(id: number): Observable<Job> {
    return this.http.get<Job>(`${this.baseUrl}/jobs/id/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // GET
  GetJobs(): Observable<Job> {
    return this.http.get<Job>(`${this.baseUrl}/jobs/`)
      .pipe(retry(1), catchError(this.errorHandler));
  }

  // PUT
  UpdateJob(id: number, data: any): Observable<Job> {
    return this.http.put<Job>(
      `${this.baseUrl}api/jobs/id/`,
      JSON.stringify(data),
      this.httpOptions
    ).pipe(retry(1), catchError(this.errorHandler));
  }

  // DELETE
  DeleteJob(id: number): Observable<Job> {
    return this.http.delete<Job>(`${this.baseUrl}/jobs/id/`, this.httpOptions)
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
      errorMessage = `Error code: ${error.status} Message: ${error.message}`;
    }

    return throwError(() => {
      return errorMessage
    });
  }
}
