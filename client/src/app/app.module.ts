import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DeviceModule } from './device/device.module';
import { NavbarComponent } from './shared/components/navbar/navbar.component';
import { ServiceOrderModule } from './service-order/service-order.module';
import { JobModule } from './job/job.module';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    DeviceModule,
    ServiceOrderModule,
    JobModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
