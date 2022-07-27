import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from  '../app-routing.module';
import { AddJobComponent } from './components/add-job/add-job.component';
import { ListJobComponent } from './components/list-job/list-job.component';
import { EditJobComponent } from './components/edit-job/edit-job.component';
import { JobService } from './services/job.service';



@NgModule({
  declarations: [
    AddJobComponent,
    ListJobComponent,
    EditJobComponent
  ],
  providers: [JobService],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ]
})
export class JobModule { }
