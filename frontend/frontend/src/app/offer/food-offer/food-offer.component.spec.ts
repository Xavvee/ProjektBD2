import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FoodOfferComponent } from './food-offer.component';

describe('FoodOfferComponent', () => {
  let component: FoodOfferComponent;
  let fixture: ComponentFixture<FoodOfferComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FoodOfferComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FoodOfferComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
