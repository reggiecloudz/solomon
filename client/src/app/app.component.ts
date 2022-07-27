import { Component } from '@angular/core';
import users from "./shared/users";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';
  client = users.getLuluWright();
}
