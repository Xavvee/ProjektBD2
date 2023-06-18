import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuAddToReservationComponent } from './menu-add-to-reservation.component';

describe('MenuAddToReservationComponent', () => {
  let component: MenuAddToReservationComponent;
  let fixture: ComponentFixture<MenuAddToReservationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MenuAddToReservationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MenuAddToReservationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
