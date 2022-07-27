import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from  '../app-routing.module';
import { AddServiceOrderComponent } from './components/add-service-order/add-service-order.component';
import { EditServiceOrderComponent } from './components/edit-service-order/edit-service-order.component';
import { ListServiceOrderComponent } from './components/list-service-order/list-service-order.component';
import { ServiceOrderService } from './services/service-order.service';

@NgModule({
  declarations: [
    AddServiceOrderComponent,
    EditServiceOrderComponent,
    ListServiceOrderComponent
  ],
  providers: [ServiceOrderService],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ]
})
export class ServiceOrderModule { }
